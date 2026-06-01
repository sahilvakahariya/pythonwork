# Write a Python program to read the contents of a file and print them on the console.
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
# Write a Python program to write multiple strings into a file. 
file = open("data.txt", "w")
file.write("This is the first line.\n")
file.write("This is the second line.\n")
file.write("This is the third line.\n")
file.close()
print("Multiple lines written successfully.")

# Write a Python program to create a file and print the string into the file.
file = open("output.txt", "w")
file.write("Hello, this is a sample string written to the file.")
file.close()
print("String written to file successfully.")

# Write a Python program to read a file and print the data on the console. 
file = open("output.txt", "r")
data = file.read()
print(data)
file.close()

# Write a Python program to check the current position of the file cursor using tell(). 
file = open("output.txt", "r")
print("Current file cursor position:", file.tell())
file.close()

