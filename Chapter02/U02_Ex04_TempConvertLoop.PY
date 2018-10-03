# TempLoop.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 05 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 4
# Soource: Python Programming
# Chapter: 2
#
# Program Description
# Convert temperature 5 times
#
# Algorithm (pseudocode)
# Print Introduction
# Loop functions
# Get input
# Convert input
# Print conversion

# Print Introduction
print("This program converts temperature from Celsius to Fahrenheit")
# Loop functions
def main():
    for i in range(5):
        # Get input
        celsius = eval(input("Enter C to convert: "))
        # Convert input
        fahrenheit = 9 / 5 * celsius + 32
        # Print conversion
        print(celsius, "C is equivalent to", fahrenheit, "F")

main()
