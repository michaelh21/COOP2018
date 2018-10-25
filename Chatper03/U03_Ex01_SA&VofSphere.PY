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
# Calculate the volume and surface area of a sphere from a radius
#
# Algorithm (pseudocode)
# Print Introduction
# Get input for radius
# Calculate the volume by cubing the radius and multiplying it by pi and 4/3
# Calculate the surface area by squaring the radius and multiplying it by pi and 4
# Print both

import math
def main():
    # Print Introduction
    print("This program calculates volume and surface area of a sphere")

    # Get input for radius
    radius = eval(input("Enter the radius: "))

    # Calculate the volume by cubing the radius and multiplying it by pi and 4/3
    volume = radius*radius*radius*(4/3)*math.pi

    # Calculate the surface area by squaring the radius and multiplying it by pi and 4
    surface = radius*radius*math.pi*4

    # Print both
    print("Using the given radius:", radius, ",the volume of the sphere is", volume, "and the surface area is:", surface)
main()
