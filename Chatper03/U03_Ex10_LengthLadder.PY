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
# Determine the length of a ladder from the height and angle from user input
#
# Algorithm (pseudocode)
# Print Introduction
# Get inputs
# Calculate the length needed by dividing height by the angle
# Print the length along with te height and the angle given


def main():
    # Print Introduction
    print("This program calculates the length of a ladder required to reach a given height")

    # Get inputs
    height = eval(input("Enter the height: "))
    angle = eval(input("Enter the angle: "))

    # Calculate the length needed by dividing height by the angle
    length = height/angle

    # Print the length
    print("The length from the height", height, "and the angle", angle, "needs to be ", length)
main()

