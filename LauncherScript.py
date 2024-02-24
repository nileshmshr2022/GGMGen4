import subprocess
import os

def is_python_installed():
    """Checks if Python is installed and accessible in the PATH."""
    try:
        return subprocess.check_output(["where", "python"], encoding="utf-8").strip()
    except subprocess.CalledProcessError:
        return None

def is_pywin32_installed():
    """Checks if pywin32 is installed."""
    try:
        import win32api
        print("pywin32 is installed.")
    except ImportError:
        print("pywin32 is not installed.")


def install_python(installer_path, arguments, log_path):
    """Attempts to install Python using the given installer and arguments."""
    try:
        process = subprocess.Popen([installer_path] + arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        
        with open(log_path, "a") as log_file:
            log_file.write(output)
            
        if process.returncode == 0:
            print("Python installation successful!")
        else:
            print(f"Python installation failed with error: {error.decode()}")
    except FileNotFoundError:
        print(f"Installer file not found at '{installer_path}'.")
    except PermissionError:
        print("Insufficient permissions to run the installer.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def install_pywin32(log_path):
    """Attempts to install pywin32."""
    try:
        subprocess.run(["pip", "install", "pywin32"], check=True)
        with open(log_path, "a") as log_file:
            log_file.write("pywin32 installation successful!\n")
        print("pywin32 installation successful!")
    except subprocess.CalledProcessError as e:
        with open(log_path, "a") as log_file:
            log_file.write(f"pywin32 installation failed with error: {e}\n")
        print(f"pywin32 installation failed with error: {e}")

def main():
    # Replace with your actual installer path and arguments
    installer_path = r"C:\Users\emb-nilemis\OneDrive - Embitel Technologies India Private Limited\Desktop\Work\GNN\python-3.11.8-amd64.exe"
    arguments = ["/quiet", "InstallAllUsers=1", "PrependPath=1", "Include_test=0"]

    # Check if Python is already installed
    python_path = is_python_installed()
    script_directory = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(script_directory, "installation_log.txt")

    # Log the information about the existing Python installation
    with open(log_path, "a") as log_file:
        log_file.write("Python already installed at: {}\n".format(python_path) if python_path else "Python not installed\n")

    # Install Python if not found
    if not python_path:
        install_python(installer_path, arguments, log_path)

    # Check if pywin32 is installed
    if not is_pywin32_installed():
        install_pywin32(log_path)


    # Run the timeLog.py script
        subprocess.run(["python", "TimeLog.py"])


if __name__ == "__main__":
    main()
