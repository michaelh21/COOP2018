# U06_Ex04_Cubes.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 29 Jan 2019
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 04
#   Source: Python Programming 
#   Chapter: 06
#
# Program Description
# This program returns the sum and cubes of the first x amount natural numbers, where x is the user input.
#
#
# Algorithm (pseudocode)
# Ask for user input
# Create two variables to use for the outcome
# Both variables will be in separate functions, but the loop will stay the same concept in both.
# Use the user input to loop the program that amount of times
    # Inside this loop, we can use the loop number plus one to use as natural numbers
    # Into one variable, add itself with the loop number and output the final result outside the loop
    # Into another variable, cube the loop number and add the variable into the variable each loop
#

def main():
    n = eval(input("Please enter the amount of first natural numbers you want to cube and sum: "))
    sumN(n)
    sumNCubes(n)

def sumN(n):
    sum = 0
    for i in range(n):
        sum = sum + (i+1)
    print("The sum of the first {0} natural numbers is: {1}.".format(n, sum))

def sumNCubes(n):
    cube = 0
    for i in range(n):
        cube = cube + ((i+1)**3)
    print("The sum of the first {0} natural numbers cubed is: {1}.".format(n, cube))

main()
