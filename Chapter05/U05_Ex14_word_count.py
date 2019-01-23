# U05_Ex14_word_count.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 17 Dec 2018
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 14
#   Source: Python Programming 
#   Chapter: 05
#
# Program Description
# This program accepts a user file name and outputs the amount of lines, words, and characters it has.
#
#
# Algorithm (pseudocode)
# Get input of the file name
# Open the file to a variable and read the file
# Create a loop that reads each line of the file
    # Create a loop that reads each word in each line
    # Create a loop that counts each character in each line; upper or lowercase is taken care of from lists.
        # Copy the 5.10 loop code for the counts of letters
# Create variables for the results to pour into
# Detect both upper and lower case

def main():
    file = input("Type the file name you want to word check: ")
    f = open(file, "r")

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]

    letterscap = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]

    total = 0
    count = 0
    lines = 0

    for line in f:
        lines = lines+1

        for i in range(26):
            letters1 = letters[i]
            letterscap1 = letterscap[i]
            charNum = line.count(letters1)
            charNum1 = line.count(letterscap1)
            total = total + charNum + charNum1

        words = line.split()
        for word in words:
            count = count + 1



    print("There are {2} lines, {0} characters, and {1} words.".format(total, count, lines))
    # text = f.read()
    # print(text)
main()