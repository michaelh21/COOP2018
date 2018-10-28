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
# Root original for the exact answer
# Divide the number the user wanted to root by 2
# Use user input repetitions inside for loop and substitute his variables with mine
# Input Newton's method
# Print answer and how far away the answer is from the exact answer

def main():
    # Print Introduction
    print("This program allows the user to compute a square root using the Newton's method a user input amount of times")

    # Get input for number we want to root
    broot = eval(input("Enter the number you wish to root: "))

    # Get input for loop repetitions
    loop = eval(input("Enter how many times you wish to use the Newton's method: "))

    # Root original for exact
    root = broot ** 0.5

    # Divide the number the user wanted to root by 2
    root2 = broot/2

    # Use user input repetitions inside for loop and substitute his variables with mine
    for i in range(loop):
        # Input Newton's method
        root2 = (root2 + broot/root2)/2

    # Print answer and how far away the answer is from the exact answer
    print("The 'guess'", root2, "is", abs(root-root2), "away from the answer:", root)
main()