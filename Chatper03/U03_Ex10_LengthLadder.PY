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
# Get inputs for both the height and the angle
# Convert the angle into radians using the formula (pi/180)angle
# Calculate the length needed by dividing height by the radians
# Print the length along with the height and the angle given

import math
def main():
    # Print Introduction
    print("This program calculates the length of a ladder required to reach a given height")

    # Get inputs for both the height and the angle
    height = eval(input("Enter the height: "))
    angle = eval(input("Enter the angle (in degrees): "))

    # Convert the angle into radians using the formula (pi/180)angle
    radians = (math.pi/180)*angle

    # Calculate the length needed by dividing height by the radians
    length = height/radians

    # Print the length along with the height and the angle given
    print("The length from the height", height, "and the angle", angle, "needs to be ", length)
main()
