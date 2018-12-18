# U05_Ex12_Future_value.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 07 Dec 2018
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 12
#   Source: Python Programming 
#   Chapter: 05
#
# Program Description
# This program alters the futval.py program and outputs a formatted table that displays each year in the investment.
#
#
# Algorithm (pseudocode)
# Copy the 2.6 program over
# Put the print statement in the loop
# Format the print statement to make a table with the lesson from 5.2 and 5.8
# Using the example from the problem, I can create a similar table


def main():
    # Get input
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    year = eval(input("Enter the number of years: "))

    print("")
    print("{0:10}{1:10}".format("Year", "Value"))

    # Calculate investment
    for i in range(year):
        principal = principal * (1 + apr)
        print("{0:>3}       {1:<20}".format(i+1, principal))


main()
