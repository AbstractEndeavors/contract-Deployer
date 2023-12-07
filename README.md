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

## Installation :computer:

Install Python 3.x and pip. The Smart Contract Station can be installed using pip.

```bash
download the repository and run deployer.py
```

## Usage :pencil:

First, import the module.

```python
import smart_contract_station
```

To interact with the Ethereum network, it is recommended to use an Ethereum client. You can provide your Ethereum address and the private key as environment variables.

```bash
export ETH_ADDRESS=your_address
export ETH_PRIVATE_KEY=your_private_key
```

Now you're ready to work with Ethereum contracts. Find out more in the [Modules Introduction](#modules-introduction-books) section.

## Modules Introduction :books:

### deployer.py

The central script, `deployer.py`, is designed for the development and autonomous placement of smart contracts. The script integrates compatibility, versions, imports, categorization based on launch sequence, and automated deployment of contracts. Additionally, it handles various file and graphical user interface operations.

### contractVariableManager.py

The `contractVariableManager.py` script is critical in preparing and deploying smart contracts by parsing and categorizing their components. It plays a vital role in file operations, managing data extracted from smart contracts, and in the user interface, creating dialog boxes and prompts and retrieving user inputs.

### contract_flattener.py

It includes 'node_js_installer.py and 'Flattener.py' scripts. It verifies Node.js installation, automatically installs if not found, and simplifies the file structure of contracts.

### get_initial_variables.py

The `get_initial_variables.py` script caters to the parsing of smart contract components, automating the process of securing contract data based on Solidity version, verifying required resources for contracts, and organizing everything for automated deployment.

### pragmaVariableManager.py

The `pragma_variable_manager.py` script is a pivotal part of Smart Contract Station and manages the versioning of Smart Contracts for their automated deployment.

### spdxManager.py

The `spdx_manager.py` script of Smart Contract Station deals with the management of SPDX License Identifiers in smart contracts to maintain consistency.

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
