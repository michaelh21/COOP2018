# U07_Ex11_LeapYear.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 25 Feb 2019
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 
#   Source: Python Programming 
#   Chapter: 
#
# Program Description
# This program gets user input of a year and determines if it is a leap year.
#
#
# Algorithm (pseudocode)
# Get input
# Check if there is a decimal or remainder.
#   If there is, do not use it and return a statement that says it is not a leap year.
# If the year is not divisible by 100 but divisible by four, print it is a leap year.
# If the year is divisible by 100 and 4, check if it is divisible by 400.
#   If not, then print it is not a leap year

def main():
    year = eval(input("Please input your year: "))

    if year % 4 > 0:
        print("The year {0} is not a leap year.".format(year))
    elif year % 100 > 0:
        print("The year {0} is a leap year.".format(year))
    elif year % 400 == 0:
        print("The year {0} is a leap year.".format(year))
    else:
        print("The year {0} is not a leap year.".format(year))

main()
