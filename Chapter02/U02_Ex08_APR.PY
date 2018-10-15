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
# Get input
# Calculate compounds using formula given
# Print calculations

def main():
    # Print Introduction
    print("This program calculates the future value")
    print("of a 10-year investment")

    # Get input
    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the investment rate: "))
    periods = eval(input("Enter the compounds per year: "))

    # Calculate compounds using formula given
    for i in range(10):
        principal = principal * ((rate)/periods)

    # Print calculations
    print("The value in 10 years is:", principal)

main()