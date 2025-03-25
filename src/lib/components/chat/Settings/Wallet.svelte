<script lang="ts">
    import {toast} from 'svelte-sonner';
    import {onMount, getContext} from 'svelte';

    import {user, config} from '$lib/stores';
    import {createAPIKey} from '$lib/apis/auths';


    import {copyToClipboard} from '$lib/utils';
    import Plus from '$lib/components/icons/Plus.svelte';
    import Tooltip from '$lib/components/common/Tooltip.svelte';
    import SensitiveInput from '$lib/components/common/SensitiveInput.svelte';
    import {createZCashWord, getUserWallets, updateUserWalletsById} from "$lib/apis/users";

    const i18n = getContext('i18n');

    export let saveHandler: Function;

    let showPrivateKeys = false;

    let JWTTokenCopied = false;

    let APIKey = '';
    let ZCashWordsCopied = false;
    let NearAcc = '';
    let NearPk = '';
    let ZCashPAddress = '';
    let ZCashWords = '';
    let ZCashBirthday = 1;

    const submitHandler = async () => {


        const updatedWallet = await updateUserWalletsById(localStorage.token, $user.id, {
            near_pk: NearPk,
            near_acc: NearAcc,
            zec_birthday: ZCashBirthday,
            zec_words: ZCashWords
        }).catch(
            (error) => {
                toast.error(`${error}`);
            }
        );
        console.log({
            near_pk: NearPk,
            near_acc: NearAcc,
            zec_birthday: ZCashBirthday,
            zec_words: ZCashWords
        })

        if (updatedWallet) {
            // Get Session User Info

            NearAcc = updatedWallet?.near_acc
            ZCashPAddress = updatedWallet?.zec_wallet
            NearPk = updatedWallet?.near_pk
            ZCashWords = updatedWallet?.zec_words
            return true;
        }
        return false;
    };

    const createZCashWallet = async () => {
        ZCashWords = await createZCashWord(localStorage.token);
        console.log("ZCASHWORD", ZCashWords);
        if (ZCashWords) {
            toast.success($i18n.t('ZCash Words created.'));
        } else {
            toast.error($i18n.t('Failed to create ZCash words.'));
        }
    };

    onMount(async () => {
        let wallets = await getUserWallets(localStorage.token, $user.id).catch((error) => {
            console.log(error);
            return {};
        });
        NearAcc = wallets?.near_acc
        ZCashPAddress = wallets?.zec_wallet
        NearPk = wallets?.near_pk
        ZCashWords = wallets?.zec_words
        ZCashBirthday = wallets?.zec_birthday

    });
</script>

<div class="flex flex-col h-full justify-between text-sm">
    <div class=" space-y-3 overflow-y-scroll max-h-[28rem] lg:max-h-full">
        <div class="space-y-1">
            <div class="pt-0.5">
                <div class="flex flex-col w-full">
                    <div class=" mb-1 text-xs font-medium">{$i18n.t('NEAR Address')}</div>

                    <div class="flex-1">
                        <input
                                class="w-full rounded-lg py-2 px-4 text-sm dark:text-gray-300 dark:bg-gray-850 outline-hidden"
                                type="text"
                                bind:value={NearAcc}
                                readonly
                        />
                    </div>
                </div>
            </div>

            <div class="pt-2">
                <div class="flex flex-col w-full">
                    <div class=" mb-1 text-xs font-medium">{$i18n.t('Zcash Public Address')}</div>

                    <div class="flex-1">
                        <input
                                class="w-full rounded-lg py-2 px-4 text-sm dark:text-gray-300 dark:bg-gray-850 outline-hidden"
                                type="url"
                                placeholder={$i18n.t('ZCash Public Address')}
                                bind:value={ZCashPAddress}
                                readonly
                        />
                    </div>
                </div>
            </div>
        </div>


        <hr class="border-gray-100 dark:border-gray-850 my-4"/>

        <div class="flex justify-between items-center text-sm">
            <div class="  font-medium">{$i18n.t('Wallet private keys')}</div>
            <button
                    class=" text-xs font-medium text-gray-500"
                    type="button"
                    on:click={() => {
					showPrivateKeys = !showPrivateKeys;
				}}>{showPrivateKeys ? $i18n.t('Hide') : $i18n.t('Show')}</button
            >
        </div>

        {#if showPrivateKeys}
            <div class="flex flex-col gap-4">
                <div class="justify-between w-full">
                    <div class="flex mt-2">
                        <div class="flex grid-cols-2 gap-2 mr-2">
                            <div>
                                <div class="flex justify-between w-full">
                                    <div class="self-center text-xs font-medium">{$i18n.t('NEAR Account')}</div>
                                </div>
                                <input
                                        class="w-full rounded-lg py-2 px-4 text-sm dark:text-gray-300 dark:bg-gray-850 outline-hidden"
                                        type="text"
                                        bind:value={NearAcc}
                                        required
                                />
                            </div>
                        </div>
                        <div class="w-full">
                            <div class="flex justify-between w-full">
                                <div class="self-center text-xs font-medium">{$i18n.t('NEAR private key')}</div>
                            </div>
                            <SensitiveInput bind:value={NearPk} readOnly={false}/>
                        </div>
                        <button
                                class="ml-1.5 px-1.5 py-1 dark:hover:bg-gray-850 transition rounded-lg"
                                on:click={() => {
								copyToClipboard(NearPk);
								JWTTokenCopied = true;
								setTimeout(() => {
									JWTTokenCopied = false;
								}, 2000);
							}}
                        >
                            {#if JWTTokenCopied}
                                <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 20 20"
                                        fill="currentColor"
                                        class="w-4 h-4"
                                >
                                    <path
                                            fill-rule="evenodd"
                                            d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z"
                                            clip-rule="evenodd"
                                    />
                                </svg>
                            {:else}
                                <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 16 16"
                                        fill="currentColor"
                                        class="w-4 h-4"
                                >
                                    <path
                                            fill-rule="evenodd"
                                            d="M11.986 3H12a2 2 0 0 1 2 2v6a2 2 0 0 1-1.5 1.937V7A2.5 2.5 0 0 0 10 4.5H4.063A2 2 0 0 1 6 3h.014A2.25 2.25 0 0 1 8.25 1h1.5a2.25 2.25 0 0 1 2.236 2ZM10.5 4v-.75a.75.75 0 0 0-.75-.75h-1.5a.75.75 0 0 0-.75.75V4h3Z"
                                            clip-rule="evenodd"
                                    />
                                    <path
                                            fill-rule="evenodd"
                                            d="M3 6a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h7a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1H3Zm1.75 2.5a.75.75 0 0 0 0 1.5h3.5a.75.75 0 0 0 0-1.5h-3.5ZM4 11.75a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 0 1.5h-3.5a.75.75 0 0 1-.75-.75Z"
                                            clip-rule="evenodd"
                                    />
                                </svg>
                            {/if}
                        </button>
                    </div>
                </div>
                {#if $config?.features?.enable_api_key ?? true}
                    <div class="justify-between w-full">

                        <div class="flex mt-2 ">

                            {#if ZCashWords}
                                <div class="flex grid-cols-3 gap-2 mr-2">

                                    <div class="col-span-1">
                                        <div class="flex justify-between w-full">
                                            <div class="self-center text-xs font-medium">{$i18n.t('ZCash Birthday')}</div>
                                        </div>
                                        <input
                                                class="w-full rounded-lg py-2 px-4 text-sm dark:text-gray-300 dark:bg-gray-850 outline-hidden"
                                                type="text"
                                                bind:value={ZCashBirthday}
                                                required
                                        />
                                    </div>
                                </div>
                                <div class="w-full">
                                    <div class="flex justify-between w-full">
                                        <div class="self-center text-xs font-medium">{$i18n.t('ZCash private key')}</div>
                                    </div>
                                    <SensitiveInput bind:value={ZCashWords} readOnly={false}/>
                                </div>
                            {:else}
                                <button
                                        class="flex gap-1.5 items-center font-medium px-3.5 py-1.5 rounded-lg bg-gray-100/70 hover:bg-gray-100 dark:bg-gray-850 dark:hover:bg-gray-850 transition"
                                        on:click={() => {
										createZCashWallet();
									}}
                                >
                                    <Plus strokeWidth="2" className=" size-3.5"/>

                                    {$i18n.t('Create new ZCash seed words')}</button
                                >
                            {/if}

                        <button
                                class="ml-1.5 px-1.5 py-1 dark:hover:bg-gray-850 transition rounded-lg"
                                on:click={() => {
										copyToClipboard(ZCashWords);
										ZCashWordsCopied = true;
										setTimeout(() => {
											ZCashWordsCopied = false;
										}, 2000);
									}}
                        >
                            {#if ZCashWordsCopied}
                                <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 20 20"
                                        fill="currentColor"
                                        class="w-4 h-4"
                                >
                                    <path
                                            fill-rule="evenodd"
                                            d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z"
                                            clip-rule="evenodd"
                                    />
                                </svg>
                            {:else}
                                <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 16 16"
                                        fill="currentColor"
                                        class="w-4 h-4"
                                >
                                    <path
                                            fill-rule="evenodd"
                                            d="M11.986 3H12a2 2 0 0 1 2 2v6a2 2 0 0 1-1.5 1.937V7A2.5 2.5 0 0 0 10 4.5H4.063A2 2 0 0 1 6 3h.014A2.25 2.25 0 0 1 8.25 1h1.5a2.25 2.25 0 0 1 2.236 2ZM10.5 4v-.75a.75.75 0 0 0-.75-.75h-1.5a.75.75 0 0 0-.75.75V4h3Z"
                                            clip-rule="evenodd"
                                    />
                                    <path
                                            fill-rule="evenodd"
                                            d="M3 6a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h7a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1H3Zm1.75 2.5a.75.75 0 0 0 0 1.5h3.5a.75.75 0 0 0 0-1.5h-3.5ZM4 11.75a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 0 1.5h-3.5a.75.75 0 0 1-.75-.75Z"
                                            clip-rule="evenodd"
                                    />
                                </svg>
                            {/if}
                        </button>


                        <Tooltip content={$i18n.t('new ZCash seed words')}>
                            <button
                                    class=" px-1.5 py-1 dark:hover:bg-gray-850transition rounded-lg"
                                    on:click={() => {
											createZCashWallet();
										}}
                            >
                                <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        fill="none"
                                        viewBox="0 0 24 24"
                                        stroke-width="2"
                                        stroke="currentColor"
                                        class="size-4"
                                >
                                    <path
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                            d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0 3.181 3.183a8.25 8.25 0 0 0 13.803-3.7M4.031 9.865a8.25 8.25 0 0 1 13.803-3.7l3.181 3.182m0-4.991v4.99"
                                    />
                                </svg>
                            </button>

                        </Tooltip>
                        </div>
                    </div>
                {/if}
            </div>
        {/if}
    </div>

    <div class="flex justify-end pt-3 text-sm font-medium">
        <button
                class="px-3.5 py-1.5 text-sm font-medium bg-black hover:bg-gray-900 text-white dark:bg-white dark:text-black dark:hover:bg-gray-100 transition rounded-full"
                on:click={async () => {
				const res = await submitHandler();

				if (res) {
					saveHandler();
				}
			}}
        >
            {$i18n.t('Save')}
        </button>
    </div>
</div>
