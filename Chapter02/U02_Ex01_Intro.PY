# U02_Ex00.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 29 Aug 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 1
# Soource: Python Programming
# Chapter: 2
#
# Program Description
# Print an introduction

def main():
    print("This program converts temperature from Celsius to Fahrenheit")

    celsius = eval(input("Enter C to convert: "))

    fahrenheit = 9 / 5 * celsius + 32

    print(celsius, "C is equivalent to", fahrenheit, "F")

main()




