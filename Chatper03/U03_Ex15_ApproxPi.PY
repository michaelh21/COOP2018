# 3.3.15.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 27 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 15
# Soource: Python Programming
# Chapter: 3
#
# Program Description
# Approximate pi
#
# Algorithm (pseudocode)
# Import math
# Print Introduction
# Get input
# Create for loop to bounce between positives and negatives
# Calculate the equation for pi
# Print the calculation

# Import math
import math
def main():
    # Print Introduction
    print("This program approximates pi, scaling in accuracy with the number from user input")

    # Get input
    x = eval(input("Enter the amount of terms: "))
    a = 0

    # Create for loop to bounce between positives and negatives
    for i in range (1, x+1):
        if i % 2 == 0:
            s = -1
        else:
            s = 1

        # Calculate the equation for pi
        a += s*(4/(2*i-1))

    # Print the calculation
    print(a-math.pi)

main()