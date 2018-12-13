# Finance.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 05 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 6
# Soource: Python Programming
# Chapter: 2
#
# Program Description
# Calculates future value of a user input year investment
#
# Algorithm (pseudocode)
# Print Introduction
# Get input
# Calculate investment
# Print calculation

def main():
        # Print Introduction
        print("This program calculates the future value")
        print("of a x-year investment")

        # Get input
        principal = eval(input("Enter the initial principal: "))
        apr = eval(input("Enter the annual interest rate: "))
        x = eval(input("Enter the number of years: "))

        # Calculate investment
        for i in range(x):
            principal = principal * (1+apr)

        # Print calculation
        print("The value in", x, "years is:", principal)
main()