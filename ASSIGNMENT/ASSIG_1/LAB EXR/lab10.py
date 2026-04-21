# Write a Python program to calculate grades based on percentage using if-else ladder. 
percent = float(input("Enter your percentage: "))
if percent >= 90:
    print("Grade: A+")
elif percent >= 80:
    print("Grade: A")
elif percent >= 70:
    print("Grade: B")
elif percent >= 60:
    print("Grade: C")
elif percent >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")