# U07_Ex03_Grades.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 25 Feb 2019
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 
#   Source: Python Programming 
#   Chapter: 
#
# Program Description
# This program takes a grade within the 100 point grading scale
#
#
# Algorithm (pseudocode)
# Copy paste 5.3
# Reverse greater than signs and change the numbers to match
# Change if statements proceeding the first to elif statements
# Create a new else statement that gives the user an A

def main():
    exam = eval(input("Enter the number grade of the exam: "))
    n = ""

    if exam < 60:
        grade = 0
    elif exam < 70:
        grade = 1
    elif exam < 80:
        grade = 2
    elif exam < 90:
        grade = 3
    else:
        grade = 4
        n = "n"

    letter = ["F", "D", "C", "B", "A"]
    letters = letter[grade]

    print("The student got a{1} {0} on his exam.".format(letters, n))
main()