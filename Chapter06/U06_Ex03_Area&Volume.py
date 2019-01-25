# U06_Ex03_Area&Volume.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 25 Jan 2019
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 03
#   Source: Python Programming 
#   Chapter: 06
#
# Program Description
# This program returns the value of Area and Volume from a radius that is given by the user.
#
#
# Algorithm (pseudocode)
# Write a main function and two other functions inside the main function
# Get input from main function for the radius
# Use the variable inside each function to calculate the area and volume of a sphere and print inside the function
# Return the functions to the main function

import math
def main():
    radius = eval(input("Please enter the radius of the sphere: "))
    sphereArea(radius)
    sphereVolume(radius)

def sphereArea(radius):
    area = (radius**2)*math.pi*4
    print("The area of a sphere from the radius {0} is: {1}".format(radius, area))

def sphereVolume(radius):
    volume = (radius**3)*math.pi*(4/3)
    print("The volume of a sphere from the radius {0} is: {1}".format(radius, volume))

main()
