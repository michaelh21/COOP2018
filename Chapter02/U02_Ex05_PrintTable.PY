# Table.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 31 Aug 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 5
# Soource: Python Programming
# Chapter: 2
#
# Program Description
# Print a table of conversions from Celsius into Fahrenheit
#
# Algorithm (pseudocode)
# Print Introduction
# Declare variable for C
# Create loop for 10 times
# Print C, then the conversion
# Add 10 to C


def main():
    # Print Introduction
    print("This program makes a table for every 10 degrees C into F")
    # Declare variable for C
    x = 0
    # Create loop for 10 times
    print ("C", "|", "F")
    for i in range(11):
        # Print C, then the conversion
        print(x, "|", (9/5)*x+32)
        # Add 10 to C
        x = x + 10
main()