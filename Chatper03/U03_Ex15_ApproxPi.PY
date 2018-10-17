# 3.3.15.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 27 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 15
# Soource: Python Programming
# Chapter: 3
#
# Program Description
# Approximate pi
#
# Algorithm (pseudocode)
# Import math
# Print Introduction
# Get input for the amount of terms to use and loop
# Declare pi variable
# Create for loop to bounce between positives and negatives
# This is done by using the remainder (%) of a term/2 division equation and adding one through each loop
# Calculate the equation for pi using a formula, where switch changes the negativity of the statement
# and 4/2*i-1, i being the number of times the for loop has looped.
# Print the calculation minus the actual amount

# Import math
import math


def main():
    # Print Introduction
    print("This program approximates pi, scaling in accuracy with the number from user input")

    # Get input for the amount of terms to use and loop
    terms = eval(input("Enter the amount of terms: "))

    # Declare pi variable
    pi = 0

    # Create for loop to bounce between positives and negatives
    # This is done by using the remainder (%) of a term/2 division equation and adding one through each loop
    for i in range (1, terms+1):
        if i % 2 == 0:
            switch = -1
        else:
            switch = 1

        # Calculate the equation for pi using a formula, where switch changes the negativity of the statement
        # and 4/2*i-1, i being the number of times the for loop has looped.
        pi += switch*(4/(2*i-1))

    # Print the calculation
    print("The approximation", pi, "was off by", abs(pi-math.pi)), "in relation to actual pi."


main()
