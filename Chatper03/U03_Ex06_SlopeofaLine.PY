# 3.1.6.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 25 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 6
# Soource: Python Programming
# Chapter: 3
#
# Program Description
# Calculate the slop of a line

def main():
    print("This program calculates the slope of a line")
    x1 = eval(input("Enter x1: "))
    y1 = eval(input("Enter y1: "))
    x2 = eval(input("Enter x2: "))
    y2 = eval(input("Enter y2: "))

    slope = (y2-y1)/(x2-x1)
    print("Your slope is ", slope)

main()