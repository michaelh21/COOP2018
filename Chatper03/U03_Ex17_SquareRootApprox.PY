# U03_Ex17_SquareRootApprox.PY.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 03 Oct 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 17
# Soource: Python Programming
# Chapter: 3
#
# Program Description
# Write a program to compute square roots using Newton's method
#
# Algorithm (pseudocode)
# Print Introduction
# Get input for number we want to root
# Get input for loop repetitions
# Root original for exact
# Divide original by 2
# Use repetitions inside for loop
# Input Newton's method
# Print answer and how far away the answer is

def main():
    # Print Introduction
    print("This program allows the user to compute a square root using the Newton's method a user input amount of times")

    # Get input for number we want to root
    x = eval(input("Enter the number you wish to root: "))

    # Get input for loop repetitions
    y = eval(input("Enter how many times you wish to use the Newton's method: "))

    # Root original for exact
    x1 = x ** 0.5

    # Divide original by 2
    y2 = x/2

    # Use repetitions inside for loop
    for i in range(y):
        # Input Newton's method
        y2 = (y2 + x/y2)/2

    # Print answer and how far away the answer is
    print("The 'guess'",y2, "is", abs(x1-y2), "away from the answer:", x1)
main()