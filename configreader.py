import configparser
from utils import logging,get_script_directory
import os

def write_to_file(file_path, num_hellos=1):

    if not file_path or not isinstance(file_path, str):
        raise ValueError("Please provide a valid file path (string).")

    try:
        # Open the file in append mode to avoid overwriting existing content
        with open(file_path, 'a') as file:
            # Write "Hello" the specified number of times, followed by a newline
            for _ in range(num_hellos):
                file.write("Hello\n")

        logging.debug(f"Successfully wrote 'Hello' {num_hellos} times to {file_path}")
    except IOError as e:
        logging.debug(f"Error writing to file: {e}")

config = configparser.ConfigParser()
script_directory = get_script_directory()
config_path = os.path.join(script_directory, 'config.ini')

def write_hellos():
    global config_path

    logging.debug(f"Reading {config_path}...")
    config.read(config_path) 

    if 'file_path' not in config['DEFAULT']:
        logging.debug("Error: File path not found in 'config.ini'. Please add a 'file_path' key to the DEFAULT section.")
    else:
        logging.debug("Configreader : reading config file  ...")
        file_path = config['DEFAULT'].get('file_path')
        if not isinstance(file_path, str):
            logging.debug("Error: File path in 'config.ini' must be a string.")
        else:
            file_path = file_path.rstrip().split('#')[0].strip()
            write_to_file(file_path)
    logging.debug("Configreader exit ...")

#if __name__ == "__main__":
#    write_hellos()