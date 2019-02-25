# U07_Ex05_BMI.py.py
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
# This program tells the user their BMI and their health range.
#
#
# Algorithm (pseudocode)
# Get input
# Use one line of code to calculate BMI
# Use a series of if statements to say whether they are below, average, or above usual BMI

def main():
    weight = eval(input("Please input your weight: "))
    height = eval(input("Please inout your height in inches: "))

    BMI = (weight*720)/(height**2)

    if BMI < 19:
        print("Your BMI {0} is under average and you are underweight.".format(BMI))
    elif BMI < 25:
        print("Your BMI {0} is average and you are healthy.".format(BMI))
    else:
        print("Your BMI {0} is over average and you are overweight or obese.".format(BMI))

main()
