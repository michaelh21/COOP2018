# U03_Ex16_Fibonacci.PY.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 03 Oct 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 16
# Soource: Python Programming
# Chapter: 3
#
# Program Description
# Output the number in the Fibonacci sequence that is selected by the user
#
# Algorithm (pseudocode)
# Print Introduction
# Get input
# Declare variables
# Create if statement if n is over 2, then minus 3 from it if so
# Print formula
# Else print 1

def main():
    # Print Introduction
    print("This program outputs the number in the Fibonacci sequence that is selected by the user")

    # Get input
    n = eval(input("Enter the number place in the Fibonacci sequence you want: "))

    # Declare variables
    x = 1
    y = 1
    z = 0

    # Create if statement if n is over 2, then minus 3 from it if so
    if n > 2:
        for i in range(n-3):
            if i % 2 == 0:
                x = x+y
            else:
                y = y+x
        z = x + y

        # Print formula
        print(z)

    # Else print 1
    else:
        print("1")

main()

