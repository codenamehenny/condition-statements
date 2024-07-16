#Task 1: Leap Year Checker Write a Python program that prompts the user to input a year. 
# The program should determine if the given year is a leap year or not and then display an appropriate message. 

# asks for year to be entered
year = int(input("Enter a year: "))
leapyear = " is a leap year!"
notleapyear = " is not a leap year."

# conditions to satisfy leap year definition
if (year % 4 == 0) and (year % 100 != 0):
    print(year , leapyear)
elif year % 400 == 0 :
    print(year , leapyear)
else:
    print(year , notleapyear)


    