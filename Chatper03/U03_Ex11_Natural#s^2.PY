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
# Calculate the sum of natural numbers based off user input for the amount
#
# Algorithm (pseudocode)
# Print Introduction
# Get input for n
# Calculate the sum with the numbers ** 2
# Print the sum

def main():
    # Print Introduction
    print("This program calculates the sum of natural numbers with the limit being user input")

    # Get input for n
    n = eval(input("Enter the amount you wish to sum: "))

    # Calculate the sum with the numbers ** 2
    x = 0
    y = 0
    for i in range(n):
        x = x + 1
        y = y + x ** 2

    # Print the sum
    print(y)


main()