# Fahr.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 31 Aug 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 
# Soource: Python Programming
# Chapter: 
#
# Program Description

def Fahr():
    print("This program converts temperature from Fahrenheit to Celsius")

    F = eval(input("Enter Fahrenheit to convert: "))

    C = ((F - 32) / 5) * 9

    print(F, "Fahrenheit is equivalent to", C, "Celsius")

Fahr()