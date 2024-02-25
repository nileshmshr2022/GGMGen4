import configparser

def write_hellos_to_file(file_path, num_hellos=5):
    """
    Writes the string "Hello" to a file the specified number of times.

    Args:
        file_path (str): The path to the file where to write.
        num_hellos (int, optional): The number of times to write "Hello". Defaults to 5.

    Raises:
        ValueError: If the file path is not provided or invalid.
        IOError: If there's an error opening or writing to the file.
    """

    if not file_path or not isinstance(file_path, str):
        raise ValueError("Please provide a valid file path (string).")

    try:
        # Open the file in append mode to avoid overwriting existing content
        with open(file_path, 'a') as file:
            # Write "Hello" the specified number of times, followed by a newline
            for _ in range(num_hellos):
                file.write("Hello\n")

        print(f"Successfully wrote 'Hello' {num_hellos} times to {file_path}")
    except IOError as e:
        print(f"Error writing to file: {e}")

# Read the file path from the config file
config = configparser.ConfigParser()
config.read('config.ini')  # Replace 'config.ini' with your actual config file name

# Ensure the file_path key exists in the DEFAULT section
if 'file_path' not in config['DEFAULT']:
    print("Error: File path not found in 'config.ini'. Please add a 'file_path' key to the DEFAULT section.")
else:
    # Get the file path and ensure it's a string
    file_path = config['DEFAULT'].get('file_path')
    if not isinstance(file_path, str):
        print("Error: File path in 'config.ini' must be a string.")
    else:
        # Handle potential comment and whitespace
        file_path = file_path.rstrip().split('#')[0].strip()

        # Call the function to write the hellos to the file
        write_hellos_to_file(file_path)
