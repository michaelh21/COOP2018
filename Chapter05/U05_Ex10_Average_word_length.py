# U05_Ex10_Average_word_length.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 07 Dec 2018
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 10
#   Source: Python Programming 
#   Chapter: 05
#
# Program Description
# This program gives the average word length in a sentence of user input.
#
#
# Algorithm (pseudocode)
# Copy the 5.9 program over
# Copy the letter counting code from 5.6
# Change the output to match the program

def main():
    sentence = input("Enter a sentence: ")

    sentence = sentence.lower()

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]

    total = 0
    for i in range(26):
        letters1 = letters[i]
        charNum = sentence.count(letters1)
        total = total + charNum

    words = sentence.split()

    count = 0
    for word in words:
        count = count+1

    print("There are {0} words and {1} characters in the sentence, making the average word length {2} characters.".format(count, total, total/count))

main()
