# U05_Ex08_Caesar_Cipher.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 07 Dec 2018
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 8
#   Source: Python Programming 
#   Chapter: 05
#
# Program Description
# This program allows the user to encode a line of text using a key value and a line of text. The encoding method
# is the Caesar cipher.
#
#
# Algorithm (pseudocode)
# Get the input for the key value
# Get the input for the phrase they want to encode
# Make the phrase lowercase
# I will translate the letters into numbers, adding the key value to the numbers, and converting them back into letters
# I can use an if statement before I convert the numbers back into letters to say if a number is over 26, we -25
#

def main():
    word = input("Enter a word: ")
    key = eval(input("Enter a number key for encoding: "))

    while True:
        if key > 25:
            key = key - 26

        if key < 0:
            key = key +26

        if key > -1 and key < 26:
            break

    word = word.lower()
    fill = ""

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]

    for char in word:
        charNum = ord(char)-97+key
        letters1 = letters[charNum]
        fill += letters1

    print("fill:", fill)


main()