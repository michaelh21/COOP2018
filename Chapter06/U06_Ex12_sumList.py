# U06_Ex12_sumList.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 19 Feb 2019
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 12
#   Source: Python Programming 
#   Chapter: 06
#
# Program Description
# This program takes a list of numbers and outputs the sum of the numbers in the list
#
#
# Algorithm (pseudocode)
# Copy paste 6.11
# Change the square function to add all the numbers in the list together.
# Return the total so that the main function can print it.
# Change the print line to be more appropriate to the program.

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
    Create a 0 variable to add unto
    The loop loops the amount of numbers inside the list
    The loop adds each number in the list onto the 0 variable
    :return:
    """
    total = 0
    for i in range(len(nums)):
        nums1 = nums[i]
        total = total+nums1
    return total

def main():
    """
    Pull the list and total from previous functions
    Output them with a print statement
    :return:
    """
    nums = input1()
    total = squareEach(nums)
    print("The list's sum {0} is {1}.".format(nums, total))

main()
