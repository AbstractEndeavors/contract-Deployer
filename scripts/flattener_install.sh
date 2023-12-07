#!/bin/bash

# Update package lists
sudo apt-get update

# Install required packages
sudo apt-get install -y ca-certificates curl gnupg

# Create keyring directory if it doesn't exist
sudo mkdir -p /etc/apt/keyrings

# Add the NodeSource GPG key to the keyrings
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg

# Add NodeSource repository for Node.js
NODE_MAJOR=20
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list

# Update package lists again
sudo apt-get update

# Install Node.js
sudo apt-get install nodejs -y

# Install Yarn
sudo apt install yarn -y

# Install Git
sudo apt install git -y

# Clone the Solidity Flattener repository
git clone https://github.com/poanetwork/solidity-flattener

# Change directory to solidity-flattener and install npm packages
cd solidity-flattener && npm install
