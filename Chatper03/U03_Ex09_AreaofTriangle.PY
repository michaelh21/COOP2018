# 3.1.9.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 27 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 
# Soource: Python Programming
# Chapter: 
#
# Program Description
def main():
    print("This program calculates the are of a triangle using its sides")
    a = eval(input("Enter side one: "))
    b = eval(input("Enter side two: "))
    c = eval(input("Enter side three: "))

    s = (a+b+c)/2
    x = (s*(s-a)*(s-b)*(s-c)) ** 0.5

    print("The triangle's area is ", x)

main()