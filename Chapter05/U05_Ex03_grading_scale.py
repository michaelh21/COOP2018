# U05_Ex03_grading_scale.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 07 Dec 2018
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 3
#   Source: Python Programming 
#   Chapter: 05
#
# Program Description
# This program takes a quiz score as input and outputs the corresponding letter grade.
#
#
# Algorithm (pseudocode)
# Ask the user for the exam score
# Create four if statements that signal what grade the exam is. These if statements will ascend from low to high grade.
# Under each if statement, add one to a variable. The variable will be used to determine the letter.
# After the if statements, create a list of letter grades starting with f
# The next line will consist of an output variable that grabs the first variable
# used and multiplies with the list variable
# Use string format to output

def main():
    exam = eval(input("Enter the number grade of the exam: "))
    grade = 0
    n = ""

    if exam > 60:
        grade = grade + 1
    if exam > 70:
        grade = grade + 1
    if exam > 80:
        grade = grade + 1
    if exam > 90:
        grade = grade + 1
        n = "n"

    letter = ["F", "D", "C", "B", "A"]
    letters = letter[grade]

    print("The student got a{1} {0} on his exam.".format(letters, n))
main()
