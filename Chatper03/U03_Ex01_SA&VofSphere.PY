# 3.1.1.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 25 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 1
# Soource: Python Programming
# Chapter: 3
# Program Description
# Write a program to calculate the volume and surface area of a
# sphere from its radius, given as input. Here are some formulas that might be useful.
#
# Algorithm (pseudocode)
# Print Introduction
# Get input
# Calculate the volume and surface area
# Print both

def main():
    # Print Introduction
    print("This program calculates the volume and surface area of a sphere from its radius")

    # Get input
    radius = eval(input("Enter the radius: "))

    # Calculate the volume and surface area
    x = radius*radius*radius*(4/3)*3.14
    y = radius*radius*3.14*4

    # Print both
    print("The volume is", x, "and the surface area is:", y)
main()
