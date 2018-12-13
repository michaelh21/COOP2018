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
# the amount of hydrogen, carbon, and oxegen, all given by the user
#
# Algorithm (pseudocode)
# Print Introduction
# Get three inputs for the three elements: hydrogen; carbon; oxygen
# Calculate the weight of the molecules by multiplying each element with a certain number
# Add all of it together
# Print the weight

def main():
    # Print Introduction
    print("This program computers the molecular weight of a carbohydrate")

    # Get three inputs for the three elements: hydrogen; carbon; oxygen
    hydrogen = eval(input("Enter the amount of hydrogen atoms: "))
    carbon = eval(input("Enter the amount of carbon atoms: "))
    oxygen = eval(input("Enter the amount of oxygen atoms: "))

    # Calculate the weight of the molecules by multiplying each element with a certain number
    # Add all of it together
    weight = hydrogen*1.00794+carbon*12.0107+oxygen*15.9994

    # Print the weight
    print("The molecular weight of a carbohydrate using your input,", "H:", hydrogen, "C:", carbon, "O:", oxygen, "is", weight)
main()