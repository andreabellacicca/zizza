# :princess: Introducing ZizZA: Your AI-Powered NEAR and Zcash Transaction Assistant
**Zizza is zer Zcash Agent**
----------------

ZizZA is an AI agent team that enables users to execute transactions on the NEAR and Zcash blockchains using intents and natural language commands. Our goal is to make interacting with the blockchain simpler and more accessible to everyone.
ZizZA can concatenate multiple commands, allowing the user to execute complex tasks.

![ZizZA Agent Team](zizza-ui/docs/img/zizza_wallpaper.jpeg)


**Table of Contents**
----------------
* [**Key Features**](#key-features)
* [**How ZizZA Works**](#how-zizza-works)
* [**How to run ZizZa locally**](#how-to-run-zizza-locally)
* [**Benefits of ZizZA**](#benefits-of-zizza)
* [**Using Natural Language to Interact with ZizZA**](#using-natural-language-to-interact-with-zizza)
* [**The AI Team: How it Works**](#the-ai-team-how-it-works)
  + [Assistant 1: ZizZA Help Desk](#assistant-1-zizza-help-desk)
  + [Assistant 2: ZizZA Command Converter](#assistant-2-zizza-command-converter)
  + [Assistant 3: ZizZA Result Commenter](#assistant-3-zizza-result-commenter)
  + [How the AI Team Works](#how-the-ai-team-works)
  + [Built with Compai](#built-with-compai)
* [**Supported Commands**](#supported-commands)
  + [1. Get Wallet Summary](#1-get-wallet-summary)
  + [2. Get Balance](#2-get-balance)
  + [3. Get Supported Chains](#3-get-supported-chains)
  + [4. Get Tokens by Chain](#4-get-tokens-by-chain)
  + [5. Get Chains by Token](#5-get-chains-by-token)
  + [6. Deposit Token](#6-deposit-token)
  + [7. Withdraw Token](#7-withdraw-token)
  + [8. Swap Token](#8-swap-token)
  + [9. Get Token Price](#9-get-token-price)
  + [10. Get Best Quote for Swap](#10-get-best-quote-for-swap)
  + [11. Send Token](#11-send-token)


**Key Features**
----------------

* **Transactions with Natural Language**: ZizZA allows users to execute transactions on the NEAR and Zcash blockchains using natural language commands, such as "Send 10 wNEAR to {address} or "SWAP 5 
 ZEC tokens with wNEAR".

* **Support for NEAR Intents**: ZizZA supports NEAR intents, including:  
  + **Transfer**: send tokens from one account to another  
  + **View**: view information related to an account or smart contract  
  + **intents.near**: ZizZA makes extensive use of the **intents.near** smart contract for **deposits, swaps, and withdrawals**, ensuring seamless and efficient transaction management  

* **Support for Zcash transactions**: ZizZA supports ZEC transfers, including:  
  + **NU6**: support for the NU6 network upgrade, enabling enhanced privacy and efficiency  
  + **Inter-address transfers**: seamless transfers between **Transparent**, **Sapling**, and **Unified Addresses**, ensuring compatibility and enhanced privacy  
  + **Shielding**: ZizZa allows you to seamlessly convert transparent ZEC into shielded funds, enhancing your privacy.

* **Cross-chain interoperability**:  
  + ZizZA leverages **OmniBridge** as a cross-chain protocol to facilitate **native ZEC deposits** and support transactions across multiple blockchain networks  

* **Intuitive User Interface**: ZizZA has a user-friendly interface that allows users to interact with the NEAR and Zcash blockchains without needing in-depth technical knowledge.
* **Command Concatenation**:  ZizZA can concatenate multiple commands, allowing the user to execute complex tasks. For example, the user can say "I want to send 10 wNEAR to this address and then swap 5 wNEAR for ZEC".


**How ZizZA Works**
----------------------

1. **User Input**: the user enters a natural language command into ZizZA's user interface.
2. **Intent Processing**: ZizZA analyzes the command and identifies the user's intent (e.g. transfer, deploy, etc.).
3. **Validation**: ZizZA validates the information provided by the user and verifies that the transactions are valid and secure.
4. **Transaction Execution**: ZizZA executes the transaction on the NEAR blockchain using the NEAR API.

**Benefits of ZizZA**
----------------------
Using ZizZA provides several benefits, including:
* **Simplicity**: ZizZA makes interacting with the NEAR and Zcash blockchains simpler and more accessible to everyone.
* **Efficiency**: ZizZA automates transactions, reducing the time and errors associated with manual transactions.
* **Security**: ZizZA ensures the security of transactions through validation and verification of user-provided information.
* **Standalone service**: One of the key benefits of ZizZA is that it can be run standalone on your local machine, without requiring any external services or dependencies.
* **Improved Privacy** : By running ZizZA on your local machine, you can keep your transactions and data private, without relying on third-party services or cloud-based solutions.
* **Enhanced Security** : With ZizZA, you have full control over your transactions and data, and can ensure that your private keys and sensitive information are stored securely on your local machine.
* **Increased Accessibility** : ZizZA's natural language interface makes it easy for anyone to interact with the NEAR and Zcash networks, regardless of their technical expertise or experience with blockchain technology.
* **Flexibility** : ZizZA can be used in a variety of scenarios, from simple transactions to complex smart contract interactions, making it a versatile tool for anyone looking to interact with the NEAR blockchain.
* **Decentralization** : ZizZA allows you to interact with the NEAR and Zcash blockchains in a decentralized manner, without relying on centralized services or intermediaries.

## How to run ZizZa locally

Make sure you have Docker installed.

```bash
./run.sh
```

## Using ZizZA

To use the ZizZA agent, open your browser on localhost:8080 (default configuration) and follow these steps:

### Step 0: Create Admin Account (First-Time Login Only)

1. **If this is your first time logging in**, you will be prompted to create an admin account.
2. Enter your:
	* **Name**: your full name.
	* **Email**: your email address.
	* **Password**: create a strong and unique password for your admin account.
3. Click **Create Account** to create your admin account.

**Note:** This step is only required for first-time users. If you have already created an admin account, proceed to Step 1.

### Step 1: Setup Your Wallet

1. Go to **Settings** → **Wallet**.
2. Add your:
	* **NEAR Account ID**: enter your NEAR account ID.
	* **NEAR Private Key (PK)**: enter your NEAR private key.
	* **Zcash Mnemonics**: enter your existing BIP39 24 word phrase or generate a new one.
	* **Zcash Wallet Birthday**: Enter the Zcash block height at the time your wallet was created. Otherwise, syncing will take longer as it starts from block 1.
3. Click **Save** to save your wallet settings.

**Note:** Please be aware that all wallet information, including private keys and addresses, is stored **locally** on your device and is **not** shared with anyone, including the **zizza-blockchain-intent-server** or any third-party services. Your wallet information remains confidential and secure, and is only used to facilitate transactions on your behalf.

### Step 2: Start a Conversation with the Agent

1. Start a conversation with the agent.
2. Ask the agent to perform actions using the following commands:
	* [List the available commands, e.g. "send NEAR", "send Zcash", "check balance", etc.]

Note: The agent will respond accordingly based on the commands you provide.

## Tips and Reminders

* Make sure to save your wallet settings to ensure that your transactions are processed correctly.
* Be careful when entering your private keys and wallet addresses, as they are sensitive information.
* If you have any issues or concerns, refer to the [list the troubleshooting or support resources, e.g. FAQ, support email, etc.].

## Installation
Follow these steps to install ZizZA as a dockerfrom terminal:
1. git clone https://github.com/andreabellacicca/zizza.git
2. cd zizza
3. git submodule update --remote --recursive
4. ./run.sh

**Using Natural Language to Interact with ZizZA**
----------------------
ZizZA allows you to interact with the NEAR and Zcash blockchains using natural language commands. You can phrase your requests in a way that feels most natural to you, and ZizZA will understand what you want to do.

For example, instead of using the specific command swap with the required parameters, you can simply say:

"I need to swap 10 wNEAR on the NEAR chain with ZEC"
"Can you exchange 5 wNEAR for ZEC on the NEAR blockchain?"
"I want to trade 10 wNEAR for ZEC on the NEAR chain"
"Swap 10 wNEAR for ZEC on the NEAR blockchain, please"

ZizZA will understand that you want to perform a swap operation, and will automatically extract the necessary parameters from your request to create a NEAR intent, such as:
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
By using natural language, you can interact with ZizZA in a more intuitive and user-friendly way, without having to remember specific command syntax or parameters.

Moreover, ZizZA can concatenate multiple commands, allowing the user to execute complex tasks. For example, the user can say "I want to send 10 wNEAR to this address and then swap 5 wNEAR for ZEC".

## Components of Zizza

1. **UI: A Conversational AI Interface**
   The user experience (UX) of Zizza is designed to be intuitive and easy to use, allowing users to chat and interact with the platform in a natural and effortless way. This component is focused on providing a straightforward and simple interface that makes it easy for users to navigate and achieve their goals.

2. **AI Agents Team**
   The AI Agents team is a critical component of Zizza, responsible for interacting with users to understand their needs and transform their commands into near intentions . These AI agents engage in conversations with users to clarify their requests, ask follow-up questions, and gather necessary information. They then analyze the user's input and convert it into a clear and actionable intents, allowing the platform to provide accurate and relevant responses or take the necessary actions
3. **Intent Blockchain Server**
   The Intent Blockchain Server is the backbone of Zizza's infrastructure, providing a secure  platform for is an application designed to handle operations such as wallet creation, deposit, swap, withdrawal, send and balance management based on user intents. It serves as a core component of the system architecture, ensuring efficient and secure transaction processing

![ZizZA Agent Team](/docs/img/zizza_scheme.png)


## UI: A Conversational AI Interface 
Our goal is to provide a seamless and intuitive user experience, similar to that of ChatGPT, where users can engage in natural-sounding conversations with our AI team.

![ZizZA Agent Team](/docs/img/ux_owui.png)

### Key Features
* **Conversational** Interface : Engage in chat-like conversations with our AI model, using a simple and intuitive text-based interface.
* **Open Web UI** : Built on top of the [Open Web UI framework](https://github.com/open-webui/open-webui), ensuring a fast, responsive, and scalable architecture.
* **Customizable** : Easily customize the interface to suit your needs, with a wide range of configuration options available.



**The AI Team: How it Works**
--------------------------------------
![ZizZA Agent Team](/docs/img/zizza_team.png)

The AI team of ZizZA is composed of three LLM (Large Language Model) assistants based on LLaMA 70B, each with a specific and complementary role. This team works together to provide a seamless user experience and support interactions with the NEAR blockchain.

### Assistant 1: ZizZA Help Desk

The ZizZA Help Desk assistant is the primary point of contact with the user. Its role is to:

* Interact with the user and understand what commands they want to execute
* Analyze the user's requests and identify the necessary parameters to execute the command
* Provide support and help if parameters are missing or the request is unclear
* Answer user questions and provide information about the NEAR blockchain and supported commands

### Assistant 2: ZizZA Command Converter

The ZizZA Command Converter assistant is responsible for converting user commands into instructions that the NEAR blockchain can execute. Its role is to:

* Analyze user commands and identify the necessary actions to execute them
* Convert commands into specific instructions for the NEAR blockchain
* Verify that the instructions are correct and complete before sending them to the blockchain

### Assistant 3: ZizZA Result Commenter

The ZizZA Result Commenter assistant is responsible for commenting on the results of actions executed on the NEAR blockchain. Its role is to:

* Analyze the results of actions executed and identify errors or anomalies
* Comment on the results and provide an explanation of what happened
* Suggest a possible solution if an error or issue occurs
* Provide additional information about the NEAR blockchain and supported commands

### How the AI Team Works
        
                    +---------------------------------------------------+
                    |                                                   |
                    | ZizZA AI Team              +-----------+          |
                    |                            |           |          |
                    |                            |   Agent   |          |
                    |                       +----> Help Desk |          |
                    |                       |    |           |          |
                    |                       |    |           |          |
                    |                       |    +-----------+          |
                    |       +------------+  |    +-----------+          |
            User    |       |            |  |    |           |          |
            Question|       |   Agent    |  |    |   Agent   |          |
            --------+------>|  Message   +--+---->  Command  |          |
                    |       | Dispatcher |  |    | Converter |          |
                    |       |            |  |    |           |          |
                    |       +------------+  |    +-----------+          |
                    |                       |    +-----------+          |
                    |                       |    |           |          |
                    |                       |    |   Agent   |          |
                    |                       +---->  Result   |          |
                    |                            | Commenter |          |
                    |                            |           |          |
                    |                            +-----------+          |
                    |                                                   |
                    +---------------------------------------------------+
              

When a user interacts with ZizZA, the AI team works together to provide a seamless user experience and support interactions with the NEAR blockchain. Here's how the process works:

1. The user sends a request to the AI team, such as "I want to send 10 wNEAR to this address".
2. The ZizZA Help Desk assistant analyzes the request and tries to understand what commands the user wants to execute.
3. The ZizZA Help Desk assistant can concatenate multiple commands, allowing the user to execute complex tasks. For example, the user can say "I want to send 10 wNEAR to this address and then swap 5 wNEAR for ZEC".
4. The ZizZA Help Desk assistant will continue to prompt the user for additional information and clarify any unclear requests until the user is ready to execute the commands.
5. Once the user is satisfied with their request, they must type "execute" to confirm that they want to proceed with the commands.
6. When the user types "execute" the Help Desk Assistant send the commands to the ZizZA Command Converter assistant.
7. The ZizZA Command Converter assistant converts the commands into specific instructions for the NEAR blockchain.
8. The ZizZA Command Converter assistant sends the instructions to the NEAR blockchain for execution.
9. The NEAR blockchain executes the instructions and sends the results to the AI team.
10. The ZizZA Result Commenter assistant analyzes the results and comments on errors or anomalies.
11. The ZizZA Result Commenter assistant suggests a possible solution if an error or issue occurs.
12. The AI team provides a response to the user with the results and additional information as needed.

### Built with Compai

The ZizZA AI team was built using Compai, a platform specifically designed for creating AI teams that collaborate with each other quickly and efficiently. Compai allows developers to create AI teams with multiple assistants, each with its own role and expertise, and to train them to work together seamlessly.

You can learn more about Compai and its features at [Compai](www.compai.team) (www.compai.team) . Compai provides a range of tools and features that make it easy to build, train, and deploy AI teams, including:

* A visual interface for designing and building AI teams
* A range of pre-built AI models and templates
* Tools for training and testing AI teams

By building the ZizZA AI team with Compai, we were able to create a highly effective and efficient AI team that provides a seamless user experience and supports interactions with the NEAR blockchain.

## zizza-blockchain-intent-server: How it works

**zizza-blockchain-intent-server** is an application designed to handle operations such as **wallet creation, deposit, swap, withdrawal, send and balance management** based on user intents. It serves as a **core component** of the system architecture, ensuring efficient and secure transaction processing.

### Main Features

* **Wallet Management**: This component handles the **creation and import** of **NEAR accounts** and **Zcash wallets**.
* **Transaction Management**: The server manages transactions related to user intentions, ensuring that every action is properly recorded and verified.
* **Intention Verification**: The server verifies user intentions before executing transactions, ensuring that they are valid and authorized.
* **Security**: The server implements robust security measures to protect sensitive information related to transactions and user intentions.
* **Scalability**: The server is designed to handle a high volume of transactions, ensuring scalability and performance even under heavy loads.

### Technical Characteristics

* **Architecture**: The server is based on a microservices architecture, allowing for flexibility and easy maintenance.
* **Technologies**: The server utilizes Python as the primary language to interact with the NEAR API SDK, ensuring efficient management of transactions and seamless integration with the NEAR blockchain. This approach leverages the simplicity and flexibility of Python, enabling the handling of complex operations in a streamlined and effective manner.  
* **Database-Free Architecture**: The solution adopts an innovative design that eliminates the need for traditional databases, reducing infrastructure complexity and enhancing scalability. All transaction-related information and user intents are managed directly on the NEAR blockchain, ensuring transparency, security, and decentralization.  
* **Zcash Integration via Wrapper**: A custom wrapper has been developed for the well-known zecwallet-light-cli wallet, enabling interaction with the Zcash blockchain without the need for a full node. This lightweight solution simplifies the process of sending, receiving, and managing Zcash transactions, making it more accessible and resource-efficient while maintaining the privacy and security features inherent to the Zcash protocol.

### Contributing

zizza-blockchain-intent-server has been developed by **wh00hw** https://github.com/wh00hw/zizza-backend/tree/master


**Supported Commands**
----------------------

ZizZA supports the following commands:

### 1. Get Wallet Summary
* **Command:** `get_wallet_summary`
* **Params:** None

### 2. Get Balance
* **Command:** `get_balance`
* **Params:**
  + `asset_symbol`: the symbol of the token to retrieve the balance for
  + `asset_chain`: the chain to use for the retrieval
  + `on_intent_contract`: a flag to indicate whether to use the NEAR intent contract (default: `true`)

### 3. Get Supported Chains
* **Command:** `get_chains`
* **Params:** None

### 4. Get Tokens by Chain
* **Command:** `get_tokens_by_chain`
* **Params:**
  + `chain`: the chain or blockchain to retrieve the tokens for

### 5. Get Chains by Token
* **Command:** `get_chains_by_token`
* **Params:**
  + `symbol`: the symbol of the token to retrieve the associated chains for

### 6. Deposit Token
* **Command:** `deposit`
* **Params:**
  + `asset_symbol`: the symbol of the token to deposit
  + `asset_chain`: the chain to use for the deposit
  + `amount`: the amount to deposit

### 7. Withdraw Token
* **Command:** `withdraw`
* **Params:**
  + `asset_symbol`: the symbol of the token to withdraw
  + `asset_chain`: the chain to use for the withdrawal
  + `amount`: the amount to withdraw
  + `native_dest_address`: the wallet address to receive the withdrawn tokens

### 8. Swap Token
* **Command:** `swap`
* **Params:**
  + `asset_in_symbol`: the symbol of the token to swap from
  + `asset_in_chain`: the chain to use for the swap from
  + `asset_out_symbol`: the symbol of the token to swap to
  + `asset_out_chain`: the chain to use for the swap to
  + `amount_in`: the amount to swap

### 9. Get Token Price
* **Command:** `get_token_price`
* **Params:**
  + `asset_symbol`: the symbol of the token to retrieve the price for
  + `asset_chain`: the chain to use for the retrieval

### 10. Get Best Quote for Swap
* **Command:** `get_best_quote`
* **Params:**
  + `asset_in_symbol`: the symbol of the token to swap from
  + `asset_in_chain`: the chain to use for the swap from
  + `asset_out_symbol`: the symbol of the token to swap to
  + `asset_out_chain`: the chain to use for the swap to
  + `amount_in`: the amount to swap

### 11. Send Token
* **Command:** `send`
* **Params:**
  + `asset_symbol`: the symbol of the token to send
  + `asset_chain`: the chain to use for the send
  + `to_address`: the wallet address to send the token to
  + `amount`: the amount to send

These commands can be used to interact with the NEAR and Zcash blockchains and perform various operations, such as retrieving balances, depositing and withdrawing tokens, swapping tokens, and sending tokens to other addresses.
