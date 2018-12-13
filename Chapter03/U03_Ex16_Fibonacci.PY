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
# Declare three variables, two of them with the value 1 and the other 0
# Create if statement if n is over 2, then create a for loop with it looping n-3 times
# Inside of the loop, create an if else statement to check if i/2 has a remainder using i % 2 == 0
# This way, sum2 will be added onto sum1, then sum1 will be added onto sum2 and so forth until the loop stops
# At the end of the loop, take sum1 and sum2 and sum them onto total
# Print the total at the end of the loop
# Else print 1

def main():
    # Print Introduction
    print("This program outputs the number in the Fibonacci sequence that is selected by the user")

    # Get input
    n = eval(input("Enter the number place in the Fibonacci sequence you want: "))

    # Declare three variables, two of them with the value 1 and the other 0
    sum1 = 1
    sum2 = 1
    total = 0

    # Create if statement if n is over 2, then create a for loop inside with it looping n-3 times
    if n > 2:
        for i in range(n-3):
            # Inside of the loop, create an if else statement to check if i/2 has a remainder using i % 2 == 0
            # This way, sum2 will be added onto sum1, then sum1 will be
            # added onto sum2 and so forth until the loop stops
            if i % 2 == 0:
                sum1 = sum1+sum2
            else:
                sum2 = sum2+sum1

        # At the end of the loop, take sum1 and sum2 and sum them onto total
        total = sum1 + sum2

        # Print the total at the end of the loop
        print("The", n, "spot in the sequence is", total)

    # Else print 1
    else:
        print("The", n, "spot in the sequence is 1")

main()

