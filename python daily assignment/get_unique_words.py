def get_unique_words(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the content of the file and split it into words
            words = file.read().split()

            # Get unique words by converting the list to a set
            unique_words = set(words)

            return sorted(unique_words)  # Sort the unique words alphabetically

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def main():
    # Input the name of the text file
    file_path = input("Enter the name of the text file: ")

    # Get and print unique words in alphabetical order
    unique_words = get_unique_words(file_path)

    if unique_words:
        print("\nUnique words in alphabetical order:")
        for word in unique_words:
            print(word)
    else:
        print("Unable to retrieve unique words.")


if __name__ == "__main__":
    main()
