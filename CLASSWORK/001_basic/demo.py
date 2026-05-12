# print hello 
# print("Hello World!..")
# print("Hello Python")

# take the value from the user
# a = input("Enter the String = ")
# print(a)

# b = input("Enter the Number = ")
# print(b)

# Varaible print using fstring (whole string ma lakhva mate)
# name = "sahil"
# email = "sahil@gmail.com"
# age = 25

# print(f"My Name is {name} and email is {email} and i am {age} years old!...")

# same sentence print karva mate => row string
# print(r"Hello World..\n\t\\n")

# #Seperator => (,) aapva mate
# print("Python","Java","Spring","Android",sep="|")

# #center ma (") aapva mate
# print("Hello \" world")

# #tab aapva mate
# print("Hello \t world")

# #statment or sentence ne merge karva mate end no use thy.
# print("Hello",end=" ")
# print("python")

# #center ma single quote or double quote mukva mate
# print("Hello ' World")
# print('Hello " World1!')

# #paragraph ne continue rakhva mate (""") triple quote no use karvo
# print("""hello
#       snifjiwed
#       sjdjsnkd
#       sbskndklsmd
#       """)

# #backspace aapva mate
# print("Hello\b \\\" \t \n python")

a=[1,2,3,[4,5,6]]
b=[6,5,4]
a.extend(b)
print(a)