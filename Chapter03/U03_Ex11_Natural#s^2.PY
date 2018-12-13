# U03_Ex11_Natural#s^2.PY.py
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
# Calculate the sum of natural numbers that are cubed based off user input for the amount of numbers
#
# Algorithm (pseudocode)
# Print Introduction
# Get input for n
# Declare a sum variable to be 0
# Create a loop that loops n times
# Add the loop (i) number ** 3 to the sum each loop
# Print the sum

def main():
    # Print Introduction
    print("This program calculates the sum of natural numbers cubed with the limit being user input")

    # Get input for n
    n = eval(input("Enter the amount of cubed numbers you wish to sum: "))

    # Declare a sum variable to be 0
    sum = 0
    # Create a loop that loops n times
    for i in range(n):
        # Add the loop (i) number ** 3 to the sum each loop
        sum = sum + ((i+1) ** 3)

    # Print the sum
    print("The sum of the first", n, "natural numbers cubed is", sum)


main()