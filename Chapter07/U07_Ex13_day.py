# U07_Ex13_day.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 01 Mar 2019
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 13
#   Source: Python Programming 
#   Chapter: 07
#
# Program Description
# This program takes user input for day, month, and year and calculates the day number.
#
#
# Algorithm (pseudocode)
# Copy 7.12
# Use the algorithm in the book to solve the problem
# Print in the main function

month = eval(input("PLease input the month in number: "))
day = eval(input("PLease input the day in number: "))
year = eval(input("PLease input the year in number: "))

def main():
    #valid = validate()
    #if valid == True:
        print("The date {0}/{1}/{2} is valid.".format(month, day, year))
    #else:
        print("The date {0}/{1}/{2} is invalid.".format(month, day, year))

def validate():
    year1 = leap()
    valid = thirty()

    if month == 2 and day == 29 and year1 == 0:
        return True
    elif month == 2 and day > 29:
        return False
    elif month > 12:
        return False
    elif day > 31:
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

def day():
    year1 = leap()
    valid = validate()
    if valid == False:
        print("The date {0}/{1}/{2} is invalid.".format(month, day, year))
    elif month == 2:
        dayNum = (31(month - 1) + day)-(4(month)+23)//10
    elif year1 == 0 and month != 1:
        dayNum = 31(month - 1) + day + 1
    else:
        dayNum = 31(month - 1) + day

    print(dayNum)

if __name__ == '__main__':
    main()
