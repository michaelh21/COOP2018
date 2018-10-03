# Finance8.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 05 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 8
# Soource: Python Programming
# Chapter: 2
#
# Program Description
# Compounds the rate of an investment per year

def main():
    print("This program calculates the future value")
    print("of a 10-year investment")

    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the investment rate: "))
    periods = eval(input("Enter the compounds per year: "))

    for i in range(10):
        principal = principal * ((rate)/periods)

    print("The value in 10 years is:", principal)

main()