import os
import subprocess
import sys
import platform

def install_nodejs_unix():
    # Installing Node.js on Unix systems
    print("Installing Node.js...")
    os.system("curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -")
    os.system("sudo apt-get install -y nodejs")

def is_node_installed():
    try:
        subprocess.run(["node", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["npm", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def main():
    if not is_node_installed():
        if platform.system() == "Linux" or platform.system() == "Darwin":  # Darwin is macOS
            install_nodejs_unix()
        else:
            print("Automatic Node.js installation is not supported for this operating system.")
            print("Please install Node.js manually.")
            sys.exit(1)

    # Rest of your script here...

if __name__ == "__main__":
    main()
