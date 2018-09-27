# 3.1.14.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 25 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: Average a series of numbers
# Soource: Python Programming
# Chapter: 3
#
# Program Description

def main():
    print("This program calculates the average of a user selected amount of numbers")
    x = eval(input("Enter how many numbers you need to average: "))
    z = 0

    for i in range(x):
       z += eval(input("Enter number(s): "))

    print("The average is ", z/x)
main()