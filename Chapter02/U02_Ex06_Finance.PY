# Finance.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 05 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 
# Soource: Python Programming
# Chapter: 
#
# Program Description

def main():
        print("This program calculates the future value")
        print("of a x-year investment")

        principal = eval(input("Enter the initial principal: "))
        apr = eval(input("Enter the annual interest rate: "))
        x = eval(input("Enter the number of years: "))

        for i in range(x):
            principal = principal * (1+apr)

        print("The value in", x, "years is:", principal)
main()