# TempLoop.py
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
    for i in range(5):
        print("This program converts temperature from Celsius to Fahrenheit")

        celsius = eval(input("Enter C to convert: "))

        fahrenheit = 9 / 5 * celsius + 32

        print(celsius, "C is equivalent to", fahrenheit, "F")

main()
