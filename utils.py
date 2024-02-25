import logging
import os,sys

def get_script_directory():
    """Get the directory of the script, considering PyInstaller executables."""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temporary directory with the bundled files
        return sys._MEIPASS
    else:
        # When running as a script, use the script's directory
        return os.path.dirname(os.path.abspath(__file__))
    
# Configure the logger
log_file_path = os.path.join(get_script_directory(),'gnnservice.log')
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')