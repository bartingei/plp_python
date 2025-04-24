try:
    with open("input.txt", 'r') as file:
        newFile = file.read()
    print(newFile)
    
    with open("newOutput.txt", 'w') as output:
        x = output.write(newFile)
    print(f"Successfully written {x} characters to newOutput.txt")
    
except FileNotFoundError:
    print("Error! input.txt not found or could not be read.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

try:
    file_name = input("Enter name of file to read: ")
    with open(file_name, 'r') as userFile:
        user = userFile.read()
    print(user)
except FileNotFoundError:
    print(f"Error! The file '{file_name}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
