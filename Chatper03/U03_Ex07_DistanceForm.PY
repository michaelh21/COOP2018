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
# Get inputs points
# Calculate the distance from the points
# Print the slope

def main():
    # Print Introduction
    print("This program calculates the distance between two points")

    # Get inputs points
    x1 = eval(input("Enter x1: "))
    y1 = eval(input("Enter y1: "))
    x2 = eval(input("Enter x2: "))
    y2 = eval(input("Enter y2: "))

    # Calculate the distance from the points
    dist = (((x2-x1) ** 2) + ((y2-y1) ** 2)) ** 0.5

    # Print the slope
    print("Your distance from", x1, ",", y1, "to", x2, ",", y2, "is", dist)
main()