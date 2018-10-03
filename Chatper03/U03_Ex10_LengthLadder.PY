# U03_Ex10_LengthLadder.PY.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 03 Oct 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 10
# Soource: Python Programming
# Chapter: 3
#
# Program Description
# Determine the length of a ladder
def main():
    print("This program calculates the length of a ladder required to reach a given height")
    x = eval(input("Enter the height: "))
    a = eval(input("Enter the angle: "))

    l = x/a

    print("The length needs to be ", l)
main()

