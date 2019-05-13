# U06_Ex09_LetterGrades.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 14 Feb 2019
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 09
#   Source: Python Programming 
#   Chapter: 06
#
# Program Description
# This program takes a quiz score as input and outputs the corresponding letter grade.
#
#
# Algorithm (pseudocode)
# Copy paste 5.3
# Make a new function for input
# Make a new function for the calculations
# Make the calculations function return a value so it can be used for printing by main

def input1():
    exam = eval(input("Enter the number grade of the exam: "))
    return exam

def calc():
    exam = input1()
    grade = 0
    if exam > 59:
        grade = grade + 1
    if exam > 69:
        grade = grade + 1
    if exam > 79:
        grade = grade + 1
    if exam > 89:
        grade = grade + 1

    return grade

def main():
    grade = calc()
    letter = ["F", "D", "C", "B", "A"]
    letters = letter[grade]

    print("The student got a {0} on his exam.".format(letters))
main()
