# U03_Ex10_LengthLadder.PY.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 03 Oct 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 10
# Soource: Python Programming
# Chapter: 3
#
# Program Description
# Determine the length of a ladder
#
# Algorithm (pseudocode)
# Print Introduction
# Get inputs
# Calculate the length needed
# Print the length
def main():
    # Print Introduction
    print("This program calculates the length of a ladder required to reach a given height")

    # Get inputs
    x = eval(input("Enter the height: "))
    a = eval(input("Enter the angle: "))

    # Calculate the length needed
    l = x/a

    # Print the length
    print("The length needs to be ", l)
main()

