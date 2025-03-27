import logging
from typing import Optional
import time
import os
from open_webui.models.auths import Auths
from open_webui.models.chats import Chats
from open_webui.models.users import (
    UserModel,
    UserRoleUpdateForm,
    Users,
    UserSettings,
    UserUpdateForm,
)

from open_webui.socket.main import get_active_status_by_user_id
from open_webui.constants import ERROR_MESSAGES
from open_webui.env import SRC_LOG_LEVELS
from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel
from open_webui.utils.auth import get_admin_user, get_password_hash, get_verified_user

from mnemonic import Mnemonic
import requests as r

ZIZZA_BLOCKCHAIN_INTENTS_SERVER_HOST = os.getenv("ZIZZA_BLOCKCHAIN_INTENTS_SERVER_HOST", "localhost")

log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS["MODELS"])

router = APIRouter()


############################
# GetUsers
############################


@router.get("/", response_model=list[UserModel])
async def get_users(
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        user=Depends(get_admin_user),
):
    return Users.get_users(skip, limit)


############################
# User Groups
############################


@router.get("/groups")
async def get_user_groups(user=Depends(get_verified_user)):
    return Users.get_user_groups(user.id)


############################
# User Permissions
############################


@router.get("/permissions")
async def get_user_permissisions(user=Depends(get_verified_user)):
    return Users.get_user_groups(user.id)


############################
# User Default Permissions
############################
class WorkspacePermissions(BaseModel):
    models: bool = False
    knowledge: bool = False
    prompts: bool = False
    tools: bool = False


class ChatPermissions(BaseModel):
    controls: bool = True
    file_upload: bool = True
    delete: bool = True
    edit: bool = True
    temporary: bool = True


class FeaturesPermissions(BaseModel):
    web_search: bool = True
    image_generation: bool = True
    code_interpreter: bool = True


class UserPermissions(BaseModel):
    workspace: WorkspacePermissions
    chat: ChatPermissions
    features: FeaturesPermissions


@router.get("/default/permissions", response_model=UserPermissions)
async def get_user_permissions(request: Request, user=Depends(get_admin_user)):
    return {
        "workspace": WorkspacePermissions(
            **request.app.state.config.USER_PERMISSIONS.get("workspace", {})
        ),
        "chat": ChatPermissions(
            **request.app.state.config.USER_PERMISSIONS.get("chat", {})
        ),
        "features": FeaturesPermissions(
            **request.app.state.config.USER_PERMISSIONS.get("features", {})
        ),
    }


@router.post("/default/permissions")
async def update_user_permissions(
        request: Request, form_data: UserPermissions, user=Depends(get_admin_user)
):
    request.app.state.config.USER_PERMISSIONS = form_data.model_dump()
    return request.app.state.config.USER_PERMISSIONS


############################
# UpdateUserRole
############################


@router.post("/update/role", response_model=Optional[UserModel])
async def update_user_role(form_data: UserRoleUpdateForm, user=Depends(get_admin_user)):
    if user.id != form_data.id and form_data.id != Users.get_first_user().id:
        return Users.update_user_role_by_id(form_data.id, form_data.role)

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=ERROR_MESSAGES.ACTION_PROHIBITED,
    )


############################
# GetUserSettingsBySessionUser
############################


@router.get("/user/settings", response_model=Optional[UserSettings])
async def get_user_settings_by_session_user(user=Depends(get_verified_user)):
    user = Users.get_user_by_id(user.id)
    if user:
        return user.settings
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ERROR_MESSAGES.USER_NOT_FOUND,
        )


############################
# UpdateUserSettingsBySessionUser
############################


@router.post("/user/settings/update", response_model=UserSettings)
async def update_user_settings_by_session_user(
        form_data: UserSettings, user=Depends(get_verified_user)
):
    user = Users.update_user_settings_by_id(user.id, form_data.model_dump())
    if user:
        return user.settings
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ERROR_MESSAGES.USER_NOT_FOUND,
        )


############################
# GetUserInfoBySessionUser
############################


@router.get("/user/info", response_model=Optional[dict])
async def get_user_info_by_session_user(user=Depends(get_verified_user)):
    user = Users.get_user_by_id(user.id)
    if user:
        return user.info
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ERROR_MESSAGES.USER_NOT_FOUND,
        )


############################
# UpdateUserInfoBySessionUser
############################


@router.post("/user/info/update", response_model=Optional[dict])
async def update_user_info_by_session_user(
        form_data: dict, user=Depends(get_verified_user)
):
    user = Users.get_user_by_id(user.id)
    if user:
        if user.info is None:
            user.info = {}

        user = Users.update_user_by_id(user.id, {"info": {**user.info, **form_data}})
        if user:
            return user.info
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ERROR_MESSAGES.USER_NOT_FOUND,
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ERROR_MESSAGES.USER_NOT_FOUND,
        )


############################
# GetUserById
############################


class UserResponse(BaseModel):
    name: str
    profile_image_url: str
    active: Optional[bool] = None


@router.get("/{user_id}", response_model=UserResponse)
async def get_user_by_id(user_id: str, user=Depends(get_verified_user)):
    # Check if user_id is a shared chat
    # If it is, get the user_id from the chat
    if user_id.startswith("shared-"):
        chat_id = user_id.replace("shared-", "")
        chat = Chats.get_chat_by_id(chat_id)
        if chat:
            user_id = chat.user_id
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ERROR_MESSAGES.USER_NOT_FOUND,
            )

    user = Users.get_user_by_id(user_id)

    if user:
        return UserResponse(
            **{
                "name": user.name,
                "profile_image_url": user.profile_image_url,
                "active": get_active_status_by_user_id(user_id),
            }
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ERROR_MESSAGES.USER_NOT_FOUND,
        )


############################
# UpdateUserById
############################


@router.post("/{user_id}/update", response_model=Optional[UserModel])
async def update_user_by_id(
        user_id: str,
        form_data: UserUpdateForm,
        session_user=Depends(get_admin_user),
):
    user = Users.get_user_by_id(user_id)

    if user:
        if form_data.email.lower() != user.email:
            email_user = Users.get_user_by_email(form_data.email.lower())
            if email_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=ERROR_MESSAGES.EMAIL_TAKEN,
                )

        if form_data.password:
            hashed = get_password_hash(form_data.password)
            log.debug(f"hashed: {hashed}")
            Auths.update_user_password_by_id(user_id, hashed)

        Auths.update_email_by_id(user_id, form_data.email.lower())
        updated_user = Users.update_user_by_id(
            user_id,
            {
                "name": form_data.name,
                "email": form_data.email.lower(),
                "profile_image_url": form_data.profile_image_url,
            },
        )

        if updated_user:
            return updated_user

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ERROR_MESSAGES.DEFAULT(),
        )

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=ERROR_MESSAGES.USER_NOT_FOUND,
    )


############################
# DeleteUserById
############################


@router.delete("/{user_id}", response_model=bool)
async def delete_user_by_id(user_id: str, user=Depends(get_admin_user)):
    if user.id != user_id:
        result = Auths.delete_auth_by_id(user_id)

        if result:
            return True

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=ERROR_MESSAGES.DELETE_USER_ERROR,
        )

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=ERROR_MESSAGES.ACTION_PROHIBITED,
    )


############################
# WALLETS
############################


class UserWallet(BaseModel):
    near_acc: Optional[str] = None
    zec_ua: Optional[str] = None
    near_pk: Optional[str] = None
    zec_words: Optional[str] = None
    zec_birthday: Optional[int] = None


@router.get("/{user_id}/wallets", response_model=UserWallet)
async def get_user_wallet(user_id: str, user=Depends(get_verified_user)):
    # Check if user_id is a shared chat
    # If it is, get the user_id from the chat
    if user_id.startswith("shared-"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ERROR_MESSAGES.USER_NOT_FOUND,
        )

    user_found = Users.get_user_by_id(user_id)

    if user_found.id == user.id:
        return UserWallet(
            **{
                "near_acc": user.near_acc,
                "zec_ua": user.zec_ua,
                "near_pk": user.near_pk,
                "zec_words": user.zec_words,
                "zec_birthday": user.zec_birthday
            }
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ERROR_MESSAGES.USER_NOT_FOUND,
        )

class UpdateWallet(BaseModel):
    data: UserWallet
    response: dict
    error: Optional[str] = None

@router.post("/{user_id}/wallets/update", response_model=Optional[UpdateWallet])
async def update_user_wallets_by_id(
        user_id: str,
        form_data: UserWallet,
        user=Depends(get_verified_user)
):
    user_found = Users.get_user_by_id(user_id)
    print(f"Form data: {form_data}")
    if user_found.id == user.id:
        if form_data.near_pk != user.near_pk or form_data.near_acc != user.near_acc:
            near_pk_updated = Users.update_user_near_pk_by_id(user.id, form_data.near_pk, form_data.near_acc)
            if not near_pk_updated:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=ERROR_MESSAGES.USER_NOT_FOUND,
                )
        if form_data.zec_words.lower() != user.zec_words or form_data.zec_birthday != user.zec_birthday:
            zec_words_updated = Users.update_user_zec_words_by_id(user.id, form_data.zec_words.lower(),
                                                                  form_data.zec_birthday)
            if not zec_words_updated:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=ERROR_MESSAGES.USER_NOT_FOUND,
                )
        user_new = Users.get_user_by_id(user_id)
        data = [{
            "command": "set_agent",
            "params": {
                "near_account_id": user_new.near_acc,
                "near_ed25519_key": user_new.near_pk,
                "zec_mnemonics": user_new.zec_words,
                "zec_wallet_birthday": user_new.zec_birthday
            }}
        ]
        response = r.post(f"http://{ZIZZA_BLOCKCHAIN_INTENTS_SERVER_HOST}:5001/execute", json=data)
        resp = response.json()

        done = False
        while not done:
            time.sleep(1)
            check_response = r.get(f"http://{ZIZZA_BLOCKCHAIN_INTENTS_SERVER_HOST}:5001/status/{resp['task_id']}")
            check_json = check_response.json()
            print(f"Response: {check_json}")
            if not 'Processing' in check_json['status']:
                done = True
        print(f"Done: {check_json}")
        print(f"{check_json['results'][0]['result']['ZEC']}")
        Users.update_user_zec_address_by_id(user.id, check_json['results'][0]['result']['ZEC']['ua_addresses']['address'])
        # TODO: devo restituire i nuovi wallet pubblici
        return {
                    'data': form_data,
                    'response': {
                        'zec':{
                            'address': check_json['results'][0]['result']['ZEC']['ua_addresses']['address'],
                            'balance': check_json['results'][0]['result']['ZEC']['ua_addresses']['balance']
                        },
                        'near':{
                            'account': check_json['results'][0]['result']['NEAR']['address'],
                            'balance': check_json['results'][0]['result']['NEAR']['balance']
                        }
                    },
                    'error': None
                }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=ERROR_MESSAGES.USER_NOT_FOUND,
    )


class ZCashWord(BaseModel):
    zec_words: str


@router.post("/wallets/words", response_model=ZCashWord)
async def generate_user_wallets_by_id(
        session_user=Depends(get_verified_user),
):
    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=256)
    print(f"word {words}")
    return ZCashWord(zec_words=str(words))
