"""
try:
    with open("input.txt", 'r') as file:
        new = file.read()  
    print(new)
except FileNotFoundError:
    print("Error: input.txt not found.")

"""

# Step 1: Writing text into input.txt (this part is already done in your code)
with open("input.txt", "a") as file:
    file.write("\nHello from developer\n")
    file.write("This is your captain speaking\n")
    file.write("Captain Morgan LOL\n")
    file.write("Thank you for flying with us today\n")
    file.write("Have a lovely flight\n")

# Step 2: Reading the contents of input.txt
with open("input.txt", 'r') as data:
    alldata = data.read()

# Step 3: Count the number of words in the file
word_count = len(alldata.split())

# Step 4: Convert all text to uppercase
uppercase_data = alldata.upper()

# Step 5: Writing the processed text and word count to output.txt
with open("output.txt", 'w') as output_file:
    output_file.write("Processed Text (Uppercase):\n")
    output_file.write(uppercase_data + "\n")
    output_file.write("\nWord Count: " + str(word_count))

# Step 6: Print success message
print("Processing complete. The results are written to output.txt.")
