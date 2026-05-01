#Write a Python program to create a dictionary with student information (name, email, age, city, course, grade) and print it. Then update the student's name and print the updated dictionary.

student = {
    "name" : "sahil",
    "email" : "sahil@gmail.com",
    "age" : 20,
    "city" : "surat",
    "course" : "python",
    "greade" : "A"
}
print(student)
student.update({"name":"kenil marvawala"})
print(student)
