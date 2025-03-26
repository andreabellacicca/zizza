# :princess: Introducing ZizZA: Your AI-Powered NEAR Transaction Assistant:
**Zizza is zer ZCash Agent**
----------------

ZizZA is an AI agent team that enables users to execute transactions on the NEAR blockchain using natural language commands. Our goal is to make interacting with the blockchain simpler and more accessible to everyone.

**Table of Contents**
----------------
* [**Key Features**](#key-features)
* [**How ZizZZA Works**](#how-zizzza-works)
* [**Benefits of ZizZZA**](#benefits-of-zizzza)
* [**Using Natural Language to Interact with ZizZZA**](#using-natural-language-to-interact-with-zizzza)
* [**Supported Commands**](#supported-commands)
    + [1. Get Balance](#1-get-balance)
    + [2. Get Supported Chains](#2-get-supported-chains)
    + [3. Get Tokens by Chain](#3-get-tokens-by-chain)
    + [4. Get Chains by Token](#4-get-chains-by-token)
    + [5. Deposit Token](#5-deposit-token)
    + [6. Withdraw Token](#6-withdraw-token)
    + [7. Swap Token](#7-swap-token)
    + [8. Get Token Price](#8-get-token-price)
    + [9. Get Best Quote for Swap](#9-get-best-quote-for-swap)
    + [10. Send Token](#10-send-token)


**Key Features**
----------------

* **Transactions with Natural Language**: ZizZZA allows users to execute transactions on the NEAR blockchain using natural language commands, such as "Send 10 wNEAR to <address>" or "SWAP 5 ZEC tokens with wNEAR".
* **Support for NEAR Intents**: ZizZZA supports NEAR intents, including:
    + **Transfer**: send tokens from one account to another
    + **View**: view information related to an account or smart contract
* **Intuitive User Interface**: ZizZZA has a user-friendly interface that allows users to interact with the NEAR blockchain without needing in-depth technical knowledge.

**How ZizZZA Works**
----------------------

1. **User Input**: the user enters a natural language command into ZizZZA's user interface.
2. **Intent Processing**: ZizZZA analyzes the command and identifies the user's intent (e.g. transfer, deploy, etc.).
3. **Validation**: ZizZZA validates the information provided by the user and verifies that the transactions are valid and secure.
4. **Transaction Execution**: ZizZZA executes the transaction on the NEAR blockchain using the NEAR API.

**Benefits of ZizZZA**
----------------------

* **Simplicity**: ZizZZA makes interacting with the NEAR blockchain simpler and more accessible to everyone.
* **Efficiency**: ZizZZA automates transactions, reducing the time and errors associated with manual transactions.
* **Security**: ZizZZA ensures the security of transactions through validation and verification of user-provided information.


**Using Natural Language to Interact with ZizZZA**
----------------------
ZizZZA allows you to interact with the NEAR blockchain using natural language commands. You can phrase your requests in a way that feels most natural to you, and ZizZZA will understand what you want to do.

For example, instead of using the specific command swap with the required parameters, you can simply say:

"I need to swap 10 wNEAR on the NEAR chain with ZEC"
"Can you exchange 5 wNEAR for ZEC on the NEAR blockchain?"
"I want to trade 10 wNEAR for ZEC on the NEAR chain"
"Swap 10 wNEAR for ZEC on the NEAR blockchain, please"

ZizZZA will understand that you want to perform a swap operation, and will automatically extract the necessary parameters from your request to create a NEAR intent, such as:
asset_in_symbol: wNEAR
asset_in_chain: NEAR
asset_out_symbol: ZEC
asset_out_chain: NEAR
amount_in: 10

You can use this natural language approach for all of the supported commands, including:

"What's my balance of wNEAR on the NEAR chain?"
"Can you deposit 10 wNEAR into my account on the NEAR blockchain?"
"I want to withdraw 5 wNEAR from my account on the NEAR chain"
"What's the best quote for swapping 10 wNEAR for ZEC on the NEAR blockchain?"
By using natural language, you can interact with ZizZZA in a more intuitive and user-friendly way, without having to remember specific command syntax or parameters.

**Supported Commands**
----------------------

ZizZZA supports the following commands:

### 1. Get Balance
* **Command:** `get_balance`
* **Params:**
    + `asset_symbol`: the symbol of the token to retrieve the balance for
    + `asset_chain`: the chain to use for the retrieval
    + `on_intent_contract`: a flag to indicate whether to use the NEAR intent contract (default: `true`)

### 2. Get Supported Chains
* **Command:** `get_chains`
* **Params:** None

### 3. Get Tokens by Chain
* **Command:** `get_tokens_by_chain`
* **Params:**
    + `chain`: the chain or blockchain to retrieve the tokens for

### 4. Get Chains by Token
* **Command:** `get_chains_by_token`
* **Params:**
    + `symbol`: the symbol of the token to retrieve the associated chains for

### 5. Deposit Token
* **Command:** `deposit`
* **Params:**
    + `asset_symbol`: the symbol of the token to deposit
    + `asset_chain`: the chain to use for the deposit
    + `amount`: the amount to deposit

### 6. Withdraw Token
* **Command:** `withdraw`
* **Params:**
    + `asset_symbol`: the symbol of the token to withdraw
    + `asset_chain`: the chain to use for the withdrawal
    + `amount`: the amount to withdraw
    + `native_dest_address`: the wallet address to receive the withdrawn tokens

### 7. Swap Token
* **Command:** `swap`
* **Params:**
    + `asset_in_symbol`: the symbol of the token to swap from
    + `asset_in_chain`: the chain to use for the swap from
    + `asset_out_symbol`: the symbol of the token to swap to
    + `asset_out_chain`: the chain to use for the swap to
    + `amount_in`: the amount to swap

### 8. Get Token Price
* **Command:** `get_token_price`
* **Params:**
    + `asset_symbol`: the symbol of the token to retrieve the price for
    + `asset_chain`: the chain to use for the retrieval

### 9. Get Best Quote for Swap
* **Command:** `get_best_quote`
* **Params:**
    + `asset_in_symbol`: the symbol of the token to swap from
    + `asset_in_chain`: the chain to use for the swap from
    + `asset_out_symbol`: the symbol of the token to swap to
    + `asset_out_chain`: the chain to use for the swap to
    + `amount_in`: the amount to swap

### 10. Send Token
* **Command:** `send`
* **Params:**
    + `asset_symbol`: the symbol of the token to send
    + `asset_chain`: the chain to use for the send
    + `to_address`: the wallet address to send the token to
    + `amount`: the amount to send

These commands can be used to interact with the NEAR blockchain and perform various operations, such as retrieving balances, depositing and withdrawing tokens, swapping tokens, and sending tokens to other addresses.