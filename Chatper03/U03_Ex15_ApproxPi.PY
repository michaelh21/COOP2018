# 3.3.15.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 27 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 15
# Soource: Python Programming
# Chapter: 3
#
# Program Description
# Approximate pi

import math
def main():
    print("This program approximates pi, scaling in accuracy with the number from user input")
    x = eval(input("Enter the amount of terms: "))
    a = 0
    for i in range (1, x+1):
        if i % 2 == 0:
            s = -1
        else:
            s = 1
        a += s*(4/(2*i-1))

    print(a-math.pi)

main()