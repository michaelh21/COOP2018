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
# Calculate the average
# Print the average
def main():
    # Print Introduction
    print("This program calculates the average of a user selected amount of numbers")

    # Get input for #s to average
    x = eval(input("Enter how many numbers you need to average: "))
    z = 0

    # Calculate the average
    for i in range(x):
       z += eval(input("Enter number(s): "))

    # Print the average
    print("The average is ", z/x)
main()