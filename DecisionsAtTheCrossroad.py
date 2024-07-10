#Task 1: Code Correction You are provided with a Python script that uses conditional statements to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.

number = int(input("Enter a number: ")) # included int to indicate tyoe of variable

if number > 0:
    print("The number is positive.")
elif number == 0: # added another =
    print("The number is zero.")
else: # removed variable, negative numbers are the last option
    print("The number is negative.")