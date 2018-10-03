# Fahr.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 31 Aug 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 9
# Soource: Python Programming
# Chapter: 2
#
# Program Description
# Converts Fahrenheit into Celsius
#
# Algorithm (pseudocode)
# Print Introduction
# Get input
# Convert C to F
# Print conversion

def Fahr():
    # Print Introduction
    print("This program converts temperature from Fahrenheit to Celsius")

    # Get input
    F = eval(input("Enter Fahrenheit to convert: "))

    # Convert C to F
    C = ((F - 32) / 5) * 9

    # Print conversion
    print(F, "Fahrenheit is equivalent to", C, "Celsius")
Fahr()