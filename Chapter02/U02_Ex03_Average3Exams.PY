# 3 Exams.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 05 Sep 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 3
# Soource: Python Programming
# Chapter: 2
#
# Program Description
# Average 3 test scores from user input
#
# Algorithm (pseudocode)
# Print Introduction
# Get input
# Average inputs
# Print average

def main():
    # Print Introduction
    print("This program averages 3 test scores")
    # Get input
    x = eval(input("Enter test score 1: "))

    y = eval(input("Enter test score 2: "))

    z = eval(input("Enter test score 3: "))
    # Average inputs
    # Print average
    print((x+y+z)/3)
main()