import os
import subprocess
import time
import stat
from abstract_utilities import write_to_file, read_from_file, safe_dump_to_file
import node_js_install


def chmodIt(x):
    """
    Changes the permission of a file, making it executable. Takes the file path as argument.
    """
    st = os.stat(x)
    os.chmod(x, st.st_mode | stat.S_IEXEC)
    os.chmod(x, 0o775)
    return 'sh '+str(x)


def delFile(x):
    """
    Deletes a file. Takes the file path as argument.
    """
    os.remove(x)


def install_npm():
    """
    Installs npm by cloning the 'solidity-flattener' repository from GitHub and installing it using npm.
    """
    os.system("""git clone https://github.com/poanetwork/solidity-flattener
    cd solidity-flattener
    npm install""")


def flatten_it(originalFilePath):
    """
    Flattens a given original file structure into a simplified one. It takes the original file path and the current directory file as arguments. The function creates a new JSON configuration for the flattening process, executes the npm start command, waits for the flattened file to be created, then reads the contents of the escalated file, performs cleanup, and overwrites the original file with the flattened contents.
    """
    # Extract directory, file name, and extension from the original file path
    
    fileName = os.path.basename(originalFilePath)
    baseName, ext = os.path.splitext(fileName)
    currFileDir=os.path.dirname(originalFilePath)
    new_contract_path = os.path.join(currFileDir,fileName)
    write_to_file(file_path=new_contract_path, contents=read_from_file(originalFilePath))
    # Prepare the name and path for the flattened file
    
    flatFileName = f"{baseName}_flat{ext}"
    flatFilePath = os.path.join(currFileDir, fileName)

    # Create JSON configuration for the flattening process
    json_file = {"originalFilePath": originalFilePath,
                 "outputDir": currFileDir}
    config_path = os.path.join(os.getcwd(),'scripts','solidity-flattener')
    config_file_path = os.path.join(config_path,'config.json')
    safe_dump_to_file(data=json_file, file_path=config_file_path)

    # Execute the flattening command
    cmd = f"cd {config_path}; npm start {originalFilePath}"
    os.system(cmd)
    # Wait for the flattened file to be created
    while not os.path.exists(flatFilePath):
        time.sleep(5)
        print('Waiting on ' + flatFilePath)
    # Read the contents of the flattened file and perform clean-up
    newFlat = os.path.join(currFileDir, flatFileName)
    write_to_file(file_path=new_contract_path, contents=read_from_file(
        newFlat))
    delFile(newFlat)  # Delete the temporary flattened file
