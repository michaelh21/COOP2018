# U06_Ex07_FibonacciFunction.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 14 Feb 2019
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 07
#   Source: Python Programming 
#   Chapter: 06
#
# Program Description
# This program outputs the number in the Fibonacci sequence that is selected by the user.
#
#
# Algorithm (pseudocode)
# Copy paste Fibonacci Program
# Make input into another function
# Make calculations into a new function
# Allow the calculation function to return a value for main
# Main will print out the result

import math

def input1():
    n = eval(input("Enter the number place in the Fibonacci sequence you want: "))
    return n

def calc():
    n = input1()
    sum1 = 1
    sum2 = 1
    if n > 2:
        for i in range(n-3):
            if i % 2 == 0:
                sum1 = sum1+sum2
            else:
                sum2 = sum2+sum1

        total = sum1 + sum2

        return total

    else:
        total = 1
        return total

def main():
    total = calc()
    print("That spot in the sequence is", total)

main()

