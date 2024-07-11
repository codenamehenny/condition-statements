#Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. 
# Your code should then identify and print out the largest number among the three.

# this section is asking for the 3 numbers to compare
first_number = float(input("Enter the first number"))
second_number = float(input("Enter the second number"))
third_number = float(input("Enter the last number"))

# comparing those numbers to find largest
if first_number >= second_number and first_number >= third_number:
    largest_number = first_number
elif second_number >= first_number and second_number >= third_number:
    largest_number = second_number
else:
    largest_number = third_number

print("The largest number is" , largest_number)