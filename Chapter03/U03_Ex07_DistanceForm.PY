# 3.1.7.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 25 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 7
# Soource: Python Programming
# Chapter: 3
#
# Program Description
# Determine the distance between two user input points on a graph
#
# Algorithm (pseudocode)
# Print Introduction
# Get four input coordinates for two points
# Calculate the distance from the points by subtracting each 1D plane with another
# Square the result of both, add the result of the squares, and then root that result
# Print the distance between both points while outputting the user input

import math
def main():
    # Print Introduction
    print("This program calculates the distance between two points")

    # Get four input coordinates for two points
    x1 = eval(input("Enter x1: "))
    y1 = eval(input("Enter y1: "))
    x2 = eval(input("Enter x2: "))
    y2 = eval(input("Enter y2: "))

    # Calculate the distance from the points by subtracting each 1D plane with another
    # Square the result of both, add the result of the squares, and then root that result
    dist = math.sqrt(((x2-x1) ** 2) + ((y2-y1) ** 2))

    # Print the distance between both points while outputting the user input
    print("Your distance from", x1, ",", y1, "to", x2, ",", y2, "is", dist)
main()