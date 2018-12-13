# 3.1.6.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 25 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 6
# Soource: Python Programming
# Chapter: 3
#
# Program Description
# Calculate the slop of a line
#
# Algorithm (pseudocode)
# Print Introduction
# Get inputs points
# Calculate the slope from points
# Print the slope

def main():
    # Print Introduction
    print("This program calculates the slope of a line")

    # Get inputs points
    x1 = eval(input("Enter x1: "))
    y1 = eval(input("Enter y1: "))
    x2 = eval(input("Enter x2: "))
    y2 = eval(input("Enter y2: "))

    # Calculate the slope from points
    slope = (y2-y1)/(x2-x1)

    # Print the slope
    print("Your slope is ", slope)

main()