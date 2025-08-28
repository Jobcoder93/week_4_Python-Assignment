# File Read & Write Challenge + Error Handling

def main():
    # Ask user for input filename
    filename = input("Enter the name of the file you want to read: ")

    try:
        # Try opening the file for reading
        with open(filename, 'r') as file:
            content = file.readlines()  # Read all lines into a list

        # Modify content: here, we'll just convert all text to uppercase as an example
        modified_content = [line.upper() for line in content]

        # Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_content)

        print(f"Modified content has been written to '{new_filename}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. Please check the name and try again.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
