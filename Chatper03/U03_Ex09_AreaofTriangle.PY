# 3.1.9.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 27 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 9
# Soource: Python Programming
# Chapter: 3
#
# Program Description
# Find the area of a triangle only using its sides
#
# Algorithm (pseudocode)
# Print Introduction
# Get three input for the sides of the triangle
# Make sure each side has it's own variable
# Add every side up and dividing the sum by 2
# Calculate the area using the previous number in the given formula:
# A = math.sqrt(s(s-a)(s-b)(s-c))
# Where a, b, and c represent the sides of the triangle
# Print the area

import math
def main():
    # Print Introduction
    print("This program calculates the area of a triangle using its sides")

    # Get three input for the sides of the triangle
    # Make sure each side has it's own variable
    side1 = eval(input("Enter side one: "))
    side2 = eval(input("Enter side two: "))
    side3 = eval(input("Enter side three: "))

    # Add every side up and dividing the sum by 2
    s = (side1+side2+side3)/2

    # Calculate the area using the previous number in the given formula:
    # A = math.sqrt(s(s-a)(s-b)(s-c))
    # Where a, b, and c represent the sides of the triangle
    area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))

    # Print the area
    print("The triangle's area with sides", side1, side2, "and", side3, "is", area)
main()