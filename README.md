# Smart Contract Station: A Python tool for automated smart contract deployment and management on Ethereum
 
![header](./header.png)

**Smart Contract Station** is designed to tackle the challenges of deploying and managing smart contracts on the Ethereum Blockchain, ensuring an automated, efficient, and error-free process. This **Python-based tool** examines, extracts and structures smart contract's source code and overall metadata (including used imports and functions) to determine the sequential deployment order of contracts and their dependencies, resulting in a comprehensive system that enhances contract visibility, auditing, verification, and debugging processes.

## Table of Contents
  
1. [Introduction :notebook:](#introduction-notebook)
2. [Installation :computer:](#installation-computer)
3. [Usage :pencil:](#usage-pencil)
4. [Modules Introduction :books:](#modules-introduction-books)
     + [deployer.py](#deployerpy)
     + [contractVariableManager.py](#contractVariableManager.py)
     + [contract_flattener.py](#contract_flattener.py)
     + [get_initial_variables.py](#get_initial_variables.py)
     + [pragmaVariableManager.py](#pragmaVariableManager.py)
     + [spdxManager.py](#spdxManager.py)
5. [Contributing :handshake:](#contributing-handshake)
6. [License :scroll:](#license-scroll)

## Introduction :notebook:
  
Smart Contract Station automates the nitty-gritty of smart contracts by preparing, placing, and managing smart contracts on the Ethereum network. By analyzing the structure and hierarchy of the contracts, it allows automatic deployment in the correct order. It also assists developers in tracking, diagnosing, and fixing issues, providing a clear advantage in auditing, security assessment processes, and verification procedures on Ethereum explorers like Etherscan.

The Smart Contract Station enables you to understand the architecture of contracts and their dependencies, enhancing your ability to debug, audit and verify contracts' integrity and functionality. Every component of a contract – the 'imports' directory featuring all dependencies required by a contract, the list of all functions in 'Functions.json', constant values in 'consVals.sol', general information in 'info.json', and tracking data for the contract in 'lineTrack.json'– can be easily accessed and managed, making this tool an essential asset for anyone dealing with complex, multi-contract systems.

## Installation :computer:

Install Python 3.x and pip. The Smart Contract Station can be installed using pip.

```bash
pip install smart-contract-station
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

-It uses various methods including 'importCheck' to verify resources, 'getNames' to process contract components, and 'saveSect' and 'sendIfs' to handle contract data. The script works with modules like 'os' and 'PySimpleGUI' to handle files and provide a graphical user interface. Crucial methods include 'pragmaVerSplit' and 'getInitialVars' that handle contract variables. The 'abstract_window_manager.py' script manages windows, threads, and operations, separating GUI controls from main contract management code. Helper routines for condition checking and list manipulation exist alongside functions to handle files and JSON data. Also, the 'contractVariablesManager' class prepares file paths and other necessary components for contract deployment.

### contract_flattener.py

1) The `contract_flattener.py` component consolidates imports, clones, and installs the Solidity flattener from GitHub using npm and refines a given file structure into a simplified version.

2) The 'Flattener.py' script within 'contract_flattener.py' centrally imports, clones, and installs the Solidity flattener from GitHub using npm and modifies a given file structure into a simplified version. The script performs these operations based on a JSON configuration file providing vital details such as original file path and output directory, leading to the creation of a new JSON configuration for every flattening process. The script executes the flattening command, waits for the flattening process to complete before incorporating the flattened file into the original. In the post-flattening cleanup process, the script removes the temporary flattened file.

3) 'node_js_installer.py' is responsible for checking Node.js installation on Unix systems (including Linux and MacOS), and it performs an automatic installation if no previous installation is found. The script attempts to run 'node' and 'npm' commands and acts upon any FileNotFoundError to initiate installation. If a Unix-based system is not detected, the script advises the user to manually install Node.js. 

### get_initial_variables.py

The `get_initial_variables.py` script caters to the parsing of smart contract components, automating the process of securing contract data based on Solidity version, verifying required resources for contracts, and organizing everything for automated deployment.

### pragmaVariableManager.py

The `pragma_variable_manager.py` script is a pivotal part of Smart Contract Station and manages the versioning of Smart Contracts for their automated deployment.

### spdxManager.py

The `spdx_manager.py` script of Smart Contract Station deals with the management of SPDX License Identifiers in smart contracts to maintain consistency.

## Contributing :handshake:

Contributions are welcome! Check out our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) for more information.

## License :scroll:

Smart Contract Station is licensed under the MIT License. See [LICENSE](LICENSE) for more details.

Happy coding!
