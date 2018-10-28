# U03_Ex11_Natural#s.PY.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 03 Oct 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 11
# Soource: Python Programming
# Chapter: 3
#
# Program Description
# Calculate the sum of natural numbers based off user input for the amount
#
# Algorithm (pseudocode)
# Print Introduction
# Get input for n
# Declare a variable with the value set to 0
# Create a for-loop that loops n times
# Have the variable add onto itself with the amount of times the loop loops (i)
# Print the sum


def main():
    # Print Introduction
    print("This program calculates the sum of natural numbers with the limit being user input")

    # Get input for n
    n = eval(input("Enter the amount of natural numbers you wish to sum: "))

    # Declare a variable with the value set to 0
    sum = 0

    # Create a for-loop that loops n times
    for i in range(n):
        # Have the variable add onto itself with the amount of times the loop loops (i)
        sum = sum + i

    # Print the sum
    print("The sum of", n, "natural numbers is", sum)


main()