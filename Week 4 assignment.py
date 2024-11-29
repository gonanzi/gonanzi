#Question 1. File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
def modify_content(content):
    # Example modification: Convert the content to uppercase
    return content.upper()

def process_files(input_filename, output_filename):
    # Open the input file in read mode
    with open(input_filename, "r") as infile:
        content = infile.read()  # Read the entire content of the file
    
    # Modify the content (you can change this to any modification you need)
    modified_content = modify_content(content)
    
    # Open the output file in write mode
    with open(output_filename, "w") as outfile:
        outfile.write(modified_content)  # Write the modified content to the new file

    print(f"Content from '{input_filename}' has been modified and written to '{output_filename}'.")

# Example usage:
input_filename = "input.txt"  
output_filename = "output.txt"  

process_files(input_filename, output_filename)



#Question 2. Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read
def read_file(filename):
    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()
            print("File content successfully read:")
            print(content)
    except FileNotFoundError:
        # Handle case when the file does not exist
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        # Handle case when there are permission issues (e.g., file is read-only)
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        # Catch any other exceptions and print the error
        print(f"An error occurred: {e}")
    else:
        print("File read successfully without errors.")
    finally:
        print("File operation attempted.")

# Ask the user for a filename
filename = input("Please enter the filename you want to read: ")

# Attempt to read the file
read_file(filename)
