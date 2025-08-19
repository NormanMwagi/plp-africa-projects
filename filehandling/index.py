
try:
    with open('myfile.txt', 'r') as file:
        data = file.read()
        data.upper()
        #count words
        word_count = len(data.split())
        print(f"Word count: {word_count}")
        # write the uppercase data and word count to a new file
        with open('myfile_upper.txt', 'w') as new_file:
            new_file.write(data)
            new_file.write(f"\nWord count: {word_count}")
            print("Data processed and written to myfile_upper.txt")
except FileNotFoundError:
    print("File not found")

# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

filename = input("Enter the filename to process: ")

try:
    with open(filename, 'r') as file:
        data = file.read()
        data.upper()
        #count words
        word_count = len(data.split())
        print(f"Word count: {word_count}")
        # write the uppercase data and word count to a new file
        with open('myfile_upper.txt', 'w') as new_file:
            new_file.write(data)
            new_file.write(f"\nWord count: {word_count}")
            print("Data processed and written to myfile_upper.txt")
except FileNotFoundError:
    print("File not found")