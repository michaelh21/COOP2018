# 3.1.7.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 25 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 7
# Soource: Python Programming
# Chapter: 3
#
# Program Description
# Determine the distance between two points

def main():
    print("This program calculates the slope of a line")
    x1 = eval(input("Enter x1: "))
    y1 = eval(input("Enter y1: "))
    x2 = eval(input("Enter x2: "))
    y2 = eval(input("Enter y2: "))

    dist = (((x2-x1) ** 2) + ((y2-y1) ** 2)) ** 0.5
    print("Your distance is ", dist)
main()