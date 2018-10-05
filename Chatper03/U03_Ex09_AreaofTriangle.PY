# 3.1.9.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 27 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 9
# Soource: Python Programming
# Chapter: 3
#
# Program Description
# Find the area of a triangle only using its sides
#
# Algorithm (pseudocode)
# Print Introduction
# Get input for sides
# Calculate the area
# Print the area

def main():
    # Print Introduction
    print("This program calculates the area of a triangle using its sides")

    # Get input for sides
    a = eval(input("Enter side one: "))
    b = eval(input("Enter side two: "))
    c = eval(input("Enter side three: "))

    # Calculate the area
    s = (a+b+c)/2
    x = (s*(s-a)*(s-b)*(s-c)) ** 0.5

    # Print the area
    print("The triangle's area is ", x)

main()