# U05_Ex16_Quiz_Historgram.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 17 Dec 2018
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 16
#   Source: Python Programming 
#   Chapter: 05
#
# Program Description
# This program takes a file name as input and counts the amount of each type of quiz score. Once completed, it
# displays a graphic interface of a histogram showing how often a quiz score came up.
#
# Algorithm (pseudocode)
# Import graphics and create a GraphWin
# Get input file name
# Read the file
# Create a title
# Output numbers 0-10 spanning across the bottom
# Go line by line and count each number and output a rectangle that increases in height based on quantity
    # Correction: I thought I could count numbers, but now I must convert them into chars and count those

from graphics import *
import math

def main():
    file = input("Type the file name you want to word check: ")
    f = open(file, "r")

    win = GraphWin("Quiz Histogram", 1100, 600)
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]

    Text(Point(550, 20), "Quiz Histogram").draw(win)

    var = 0
    chars = []
    fill = ""

    for i in range(11):
        Text(Point(100*i+50, 550), i).draw(win)
        for line in f:
            Num = int(line)
            chars = chr(Num+97)
            fill += chars
        letters1 = letters[i]
        count = fill.count(letters1)
        Rectangle(Point(100*i+75, 500-count*30), Point(100*i+25, 500)).draw(win)

    win.getMouse()
    win.close()

main()
