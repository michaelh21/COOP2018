# U06_Ex11_squareEach(nums).py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 14 Feb 2019
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 11
#   Source: Python Programming 
#   Chapter: 06
#
# Program Description
# This program squares a number list
#
#
# Algorithm (pseudocode)
# Make a list of numbers to square
# Make functions input, main and squareEach
# Pull from the list made by the user in the input function and use it in the squareEach function
# In the main function, I will pull the returns from all previous functions and formally print them.

def input1():
    """
    Ask for the amount of numbers to put inside the list
    Loop for that many times and inside the loop we add the input into the list
    Return the list
    :return:
    """
    nums = list()
    amount = eval(input("Enter the amount of numbers you want to enter: "))
    for i in range(amount):
        nums.append(eval(input("Enter a number to add to the list: ")))
    return nums

def squareEach(nums):
    """
    Pull the list from input function
    Loop the amount of numbers in the list to square them and add them to another list
    Return the changed list
    :return:
    """
    total = list()
    for i in range(len(nums)):
        nums1 = nums[i]
        nums1 = nums1*nums1
        total.append(nums1)
    return total

def main():
    """
    Pull the lists from both previous functions
    Output them with a print statement
    :return:
    """
    nums = input1()
    print("The list {0} squared is {1}.".format(nums, squareEach(nums)))

main()