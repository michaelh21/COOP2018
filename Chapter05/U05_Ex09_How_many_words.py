# U05_Ex09_How_many_words.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 07 Dec 2018
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 9
#   Source: Python Programming 
#   Chapter: 05
#
# Program Description
# This program gives a word count for a sentence the user inputs.
#
#
# Algorithm (pseudocode)
# Get sentence from user
# Make everything lowercase
# Use the split function to separate words
# Create a for loop that counts how many words are in sentence

def main():
    sentence = input("Enter a sentence: ")

    sentence = sentence.lower()

    words = sentence.split()

    count = 0

    for word in words:
        count = count+1

    print("There are {0} words in that sentence.".format(count))
main()
