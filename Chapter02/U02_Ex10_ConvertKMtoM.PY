# KMM.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 31 Aug 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 10
# Soource: Python Programming
# Chapter: 2
#
# Program Description
# Convert Kilometers into miles
#
# Algorithm (pseudocode)
# Print Introduction
# Get input
# Convert
# Print conversion

def main():
    # Print Introduction
    print("This program converts distance from Kilometers to Miles")

    # Get input
    KM = eval(input("Enter Kilometers to convert: "))

    # Convert
    M = KM * 0.621371

    # Print conversion
    print(KM, "KM is equivalent to", M, "Miles")

main()