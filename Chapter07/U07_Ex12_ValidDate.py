# U07_Ex12_ValidDate.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 27 Feb 2019
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 12
#   Source: Python Programming 
#   Chapter: 07
#
# Program Description
# This program accepts user input for a date to check if it is valid.
#
#
# Algorithm (pseudocode)
# Get user input
# For ease, use global variables when working with multiple functions
# Check if the user user February and 29 as the day, if so:
#   Check if the year is a leap year using 7.11 code
# Check the months if they have 30 or 31 days, maybe using a list or function
# Return values to main for printing

month = eval(input("PLease input the month in number: "))
day = eval(input("PLease input the day in number: "))
year = eval(input("PLease input the year in number: "))

def setInput(m, d, y):
    global month, day, year
    month = m
    day = d
    year = y


def main():
    valid = validate()
    if valid == True:
        print("The date {0}/{1}/{2} is valid.".format(month, day, year))
    else:
        print("The date {0}/{1}/{2} is invalid.".format(month, day, year))

def validate(m, d, y):
    setInput(month, day, year)
    year1 = leap()
    valid = thirty()

    if month == 2 and day == 29 and year1 == 0:
        return True
    elif month == 2 and day > 29:
        return False
    elif month > 12 or day > 31:
        return False
    elif day == 31 and valid == 0:
        return True
    elif day < 31 and month < 13:
        return True
    else:
        return False

def leap():
    if year % 4 > 0:
        year1 = 1
    elif year % 100 > 0:
        year1 = 0
    elif year % 400 == 0:
        year1 = 0
    else:
        year1 = 1

    return year1

def thirty():
    valid = 1
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 and day == 31:
        valid = 0
    elif month != 1 or month != 3 or month != 5 or month != 7 or month != 8 or month != 10 or month != 12 and day == 31:
        valid = 1

    return valid


if __name__ == '__main__':
    main()