# U06_Ex06_AOT.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 29 Jan 2019
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 06
#   Source: Python Programming 
#   Chapter: 06
#
# Program Description
# This program calculates the area of a triangle from user input of it's three sides.
#
#
# Algorithm (pseudocode)
# Copy paste exercise 3.9
# Make the input into different functions
# Make the calculation into different function
# Make main the print statement in main
# For the calculation and main, I will need to pull the variables from the other functions; done with return statement

import math

def input1():
    side1 = eval(input("Enter side one: "))
    return side1

def input2():
    side2 = eval(input("Enter side two: "))
    return side2

def input3():
    side3 = eval(input("Enter side three: "))
    return side3

def calc():
    side1 = input1()
    side2 = input2()
    side3 = input3()
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area

def main():
    area = calc()
    print("The triangle's area is {0}".format(area))
main()

