# Write a program to enter marks of three subjects from the user and store them in dictionary.
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

x = int(input("Enter Phy marks: "))
marks.update({"phy" : x})

x = int(input("Enter Chem marks : "))
marks.update({"Chem" : x})

x = int(input("Enter Maths marks : "))
marks.update({"Maths" : x})

print(marks)