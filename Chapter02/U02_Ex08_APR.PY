# Finance8.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 05 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 8
# Soource: Python Programming
# Chapter: 2
#
# Program Description
# Compounds the rate of an investment per year
#
# Algorithm (pseudocode)
# Print Introduction
# Get input for initial investment, rate, and periods.
# Loop program 10 * periods
# Calculate compounds using principal multiplied by the rate divided by the amount of periods
# with 12/periods so that the compounds divide into the year
# Print calculations

def main():
    # Print Introduction
    print("This program calculates the future value")
    print("of a 10-year investment")

    # Get input for initial investment, rate, and periods.
    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the investment rate percentage: "))
    periods = eval(input("Enter the compounds per year: "))

    # Loop program 10 * periods
    for i in range(10*periods):
        # Calculate compounds using principal multiplied by the rate divided by the amount of periods
        # with the value adding onto itself
        principal = principal + principal * ((rate/100)/periods)

    # Print calculations
    print("The value in 10 years is:", principal)

main()