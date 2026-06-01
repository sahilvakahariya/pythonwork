# Write a Python program to search for a word in a string using re.search(). 
import re
text = "I am learning Python"
result = re.search("Python", text)
if result:
    print("Word Found")
else:
    print("Word Not Found")
    
# Write a Python program to match a word in a string using re.match(). 
import re
text = "Python is easy"
result = re.match("Python", text)
if result:
    print("Match Found")
else:
    print("No Match")