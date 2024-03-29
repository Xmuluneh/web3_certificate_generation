## End-to-End Web3 dApps:

### certificate generation, distribution, and value transfer with Algorand NFTs and smart contracts

## project outcomes 

In this project, the client is 10 Academy; the client would like to solve the challenge of ensuring that certificates are available to all trainees in a secure way, and (if possible) that certificate holders can benefit from smart contract actions now and in the future. At present, certificates are distributed as simple PDF files, without the ability to verify their authenticity nor can 10 Academy undertake smart actions with the trainees/their contracts.

10 Academy has partnered with Algorand to use the Algorand Blockchain as the foundational element of the NFT, and this must now be implemented. In this project you will build end-to-end Web3 dapps on the Algorand Blockchain that will help 10 Academy generate and distribute Non-Fungible Tokens (NFTs) as certificates that will represent the successful completion of a weekly challenge to trainees, and allow trainees with NFTs to interact with a smart contract to perform pre-defined actions.

## Frontend

`git clone https://github.com/Xmuluneh/web3_certificate_generation.git `

`cd web3_certificate_generation`

`npx create-react-app client  --use-npm`

## install Sandbox

Algorand provides a docker instance for setting up a node, which can be used to get started developing quickly. To install and use this instance, follow these instructions.​

`cd web3_certificate_generation`

`git clone https://github.com/algorand/sandbox.git`

`cd sandbox`

`./sandbox up testnet -v`

## Backend 

`cd web3_certificate_generation`

`pip install -r requirements.txt `

`python manage.py migrate`

`python manage.py server`
