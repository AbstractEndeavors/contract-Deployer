# Smart Contract Station: A Python tool for automated smart contract deployment and management on Ethereum
 
![header](./header.png)

**Smart Contract Station** is designed to tackle the challenges of deploying and managing smart contracts on the Ethereum Blockchain, ensuring an automated, efficient, and error-free process. This **Python-based tool** examines, extracts and structures smart contract's source code and overall metadata (including used imports and functions) to determine the sequential deployment order of contracts and their dependencies, resulting in a comprehensive system that enhances contract visibility, auditing, verification, and debugging processes.

## Table of Contents
  
1. [Introduction :notebook:](#introduction-notebook)
2. [Main Features :pencil:](#main_features-pencil)
3. [Installation :computer:](#installation-computer)
4. [Usage :pencil:](#usage-pencil)
5. [Modules Introduction :books:](#modules-introduction-books)
     + [deployer.py](#deployerpy)
     + [contractVariableManager.py](#contractVariableManager.py)
     + [contract_flattener.py](#contract_flattener.py)
     + [get_initial_variables.py](#get_initial_variables.py)
     + [pragmaVariableManager.py](#pragmaVariableManager.py)
     + [spdxManager.py](#spdxManager.py)
6. [How It Works 👓](#how_it_works-eyeglasses)
7. [Conclusion 🖋️](#how_it_works-pen)
8. [Contributing :handshake:](#contributing-handshake)
9. [License :scroll:](#license-scroll)

## Introduction :notebook:
  
Smart Contract Station automates the nitty-gritty of smart contracts by preparing, placing, and managing smart contracts on the Ethereum network. By analyzing the structure and hierarchy of the contracts, it allows automatic deployment in the correct order. It also assists developers in tracking, diagnosing, and fixing issues, providing a clear advantage in auditing, security assessment processes, and verification procedures on Ethereum explorers like Etherscan. All in play to help the user better understand the architecture of contracts and their dependencies, enhancing your ability to debug, audit and verify contracts' integrity and functionality.

## Main Features :pencil:

1. **Smart contract syntax parameters detection**: Determines various parameters such as visibility, modifiers, and global variables that underlie the contract for comprehensive analysis.
2. **Graphical user interface**: Provides efficient window management with long-running operations and imbues an interactive user-interface layer to the console-driven system.
3. **Information extraction and storage**: Assesses the contract and stores key information, offering insights into contract dependencies, structure, and functionality.
4. **Deployment process automation**: Streamlines the process of deploying including creation of requisite folders, initialization of home directories, and setting the script's starting point.

## Modules Introduction :books:

### Deployer
This core module of *Smart Contract Station* handles user interaction, checks the existence of folders and files, as well as retrieves syntax information about the contracts. It also creates necessary folders for deployment, determines the endpoint for deployment, and deploys the contracts.
[Read More](deployer.md)

### Contract Variables Manager
This script molds and prepares the components of smart contracts for deployment. It verifies resources, processes contract components, and handles the contract's data.
[Read More](contract_variables_manager.md)

### Flattener
The Flattener module simplifies the structure of the contract, importing, cloning, and installing the Solidity flattener. The Flattener script modifies a given file structure based on a JSON configuration file, thereby creating a new JSON configuration for every flattening process. 
[Read More](flattener.md)

### Initial Variables Manager
This script focuses on parsing smart contract components and saving contract data, thereby automating the process of smart contract deployment. It gathers all vital variables and information and handles various types of variables. 
[Read More](get_initial_vars.md)

### Pragma Variables Manager
This script handles the versioning of smart contracts for automated deployment. The Pragma Variables Manager processes all pragma versions, retrieves pragma version details, and ensures that every Smart Contract aligns with its respective range and order of deployment.
[Read More](pragma_variables_manager.md)

### SPDX Manager
It deals with the management of SPDX License Identifiers in smart contracts. This class fetches SPDX identifiers from contracts and compares these identifiers with a predefined list.
[Read More](spdx_manager.md)

## Installation
Follow the instructions listed below to get this project up and running on your local machine for development purposes.
```bash
# Clone the repository
git clone https://github.com/username/repo.git

# Move into the cloned repository
cd repo

# Install all dependencies
pip install -r requirements.txt

# Run the tool
python main.py
```
To interact with the Ethereum network, it is recommended to use an Ethereum client. You can provide your Ethereum address and the private key as environment variables.

```bash
export ETH_ADDRESS=your_address
export ETH_PRIVATE_KEY=your_private_key
```

Now you're ready to work with Ethereum contracts. Find out more in the [Modules Introduction](#modules-introduction-books) section.

## How It Works 👓

- Checks the existence of files and directories and prevents potential errors.
- Provides utility functions to create dialog boxes, prompts, and retrieves user inputs.
- Retrieves essential variables and information by scanning program details.
- Manages contract variables and resources, preparing the contract for deployment.
- It handles Node.js installation on Unix systems and simplifies the contract file structure.
- Ensures versioning and order of deployment for Smart Contracts.

## Conclusion 🖋️

The Smart Contract Station is a vital Python tool for the development and autonomous placement of smart contracts. This module is carved for meticulous handling of necessary procedures for contract creation and deployment. Each script ensures a well-rounded smooth process and a sturdy base for secure contract placement.


## Contributing :handshake:

Contributions are welcome! Check out our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) for more information.

## License :scroll:

Smart Contract Station is licensed under the MIT License. See [LICENSE](LICENSE) for more details.

Happy coding!
