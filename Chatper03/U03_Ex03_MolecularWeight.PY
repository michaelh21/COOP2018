# 3.1.3.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 25 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: Write a program that computes the molecular weight of a carbohydrate based on
# the number of hydrogen, carbon, and oxygen atoms in the molecule
# Source: Python Programming
# Chapter: 3
#
# Program Description

def main():
    print("This program computers the emolecular weight of a carbohydrate")
    hydrogen = eval(input("Enter the amount of hydrogen atoms: "))
    carbon = eval(input("Enter the amount of carbon atoms: "))
    oxygen = eval(input("Enter the amount of oxygen atoms: "))

    weight = hydrogen*1.00794+carbon*12.0107+oxygen*15.9994
    print("The molecular weight of a carbohydrate using your input is ", weight)
main()