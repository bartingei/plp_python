"""
Opening Files 🔓

Use Python’s open() function to access a file.
Syntax: open(filename, mode), where:
filename: The name of the file you want to work with.
mode: The mode you want to open the file in.
Modes include:
'r': Read mode, used for reading files.
'w': Write mode, creates a new file or overwrites an existing one.
'a': Append mode, adds new content without deleting existing data.
'rb', 'wb': Binary modes for non-text files, like images.
"""
"""
with open("example.txt",'w') as file:
    file.write("Welcome to python")
#opening a file and writing into it
with open("example.txt", 'r') as file:
    content = file.read()
#outputting the content written on the file 
print(content)

with open("example.txt", 'a') as file:
    file.write("\nthis is the appended text")

with open("example.txt", 'r') as file:
    new_conts = file.read()

print(new_conts)

with open("example.txt", "w") as anotherFile:
    anotherFile.write("Previous file has been cleared")

with open("example.txt", 'r') as anotherFile:
    data = anotherFile.read()

print(data)
"""
"""
Reading Files 📜

Python provides multiple ways to read file contents:
.read(): Reads the entire file.
.readline(): Reads a single line at a time.
.readlines(): Reads all lines and returns a list.
Example:

with open("example.txt", "r") as file: data = file.read() print(data)
Use cases: Processing large datasets or analyzing text documents.
"""

try:
    with open("nonexistent.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found. Please check the filename.")