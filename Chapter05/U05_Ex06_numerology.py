# U05_Ex06_numerology.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 07 Dec 2018
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 6
#   Source: Python Programming 
#   Chapter: 05
#
# Program Description
# This program calculates the value of a name by taking letters and assigning numbers to them based on their
# chronological position in the alphabet. This program can take full names as well.
#
# Algorithm (pseudocode)
# Get input for name
# Create a loop that loops 26 times to cover the alphabet
# Count which letters the name has and how many with the function s.count()
    # There needs to be a list with all the letters
    # This will serve as the rotation for the s.count()
# In the for loop, create a value that adds to itself
    # Correction: just use i from the loop statement


def main():
    name = input("Enter a name: ")
    name = name.lower()
    total = 0

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]

    for i in range(26):
        letters1 = letters[i]
        count = name.count(letters1)
        count = (i+1)*count
        total = total + count
    print("The value of the name, {0}, is {1}.".format(name, total))


main()
