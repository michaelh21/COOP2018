# 3.1.3.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 25 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 3
# the number of hydrogen, carbon, and oxygen atoms in the molecule
# Source: Python Programming
# Chapter: 3
#
# Program Description
# Write a program that computes the molecular weight of a carbohydrate based on
#
# Algorithm (pseudocode)
# Print Introduction
# Get inputs
# Calculate the weight of the molecules
# Print the weight

def main():
    # Print Introduction
    print("This program computers the emolecular weight of a carbohydrate")

    # Get inputs
    hydrogen = eval(input("Enter the amount of hydrogen atoms: "))
    carbon = eval(input("Enter the amount of carbon atoms: "))
    oxygen = eval(input("Enter the amount of oxygen atoms: "))

    # Calculate the weight of the molecules
    weight = hydrogen*1.00794+carbon*12.0107+oxygen*15.9994

    # Print the weight
    print("The molecular weight of a carbohydrate using your input is ", weight)
main()