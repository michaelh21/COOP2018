# 3.1.14.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 25 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 14
# Soource: Python Programming
# Chapter: 3
#
# Program Description
# Average a series of numbers
#
# Algorithm (pseudocode)
# Print Introduction
# Get input for #s to average
# Use that number in a loop
# Gather input inside the loop, adding the numbers onto itself
# Print the sum over the amount of numbers used
def main():
    # Print Introduction
    print("This program calculates the average of a user selected amount of numbers")

    # Get input for #s to average
    numbers = eval(input("Enter how many numbers you need to average: "))
    sum = 0

    # Use that number in a loop
    for i in range(numbers):
        # Gather input inside the loop, adding the numbers onto itself
       sum += eval(input("Enter number(s): "))

    # Print the sum over the amount of numbers used
    print("The average is ", sum/numbers)
main()