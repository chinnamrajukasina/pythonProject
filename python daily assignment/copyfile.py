# copyfile.py

def copy_file_content():
    # Prompt the user for the names of two text files
    input_file_name = input("Enter the name of the source text file: ")
    output_file_name = input("Enter the name of the destination text file: ")

    try:
        # Open the source file for reading
        with open(input_file_name, 'r') as source_file:
            # Read the content of the source file
            file_content = source_file.read()

            # Open the destination file for writing
            with open(output_file_name, 'w') as destination_file:
                # Write the content to the destination file
                destination_file.write(file_content)

        print(f"Content from '{input_file_name}' has been successfully copied to '{output_file_name}'.")

    except FileNotFoundError:
        print("Error: One or both of the specified files not found.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    copy_file_content()
