# U05_Ex15_Exam_Graph.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 17 Dec 2018
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 15
#   Source: Python Programming 
#   Chapter: 05
#
# Program Description
# This program gets input from a file and plots the exam scores in a horizontal bar graph using a graphics UI.
#
#
# Algorithm (pseudocode)
# Copy paste 4.7 - Circle Program
# Get input for the file
# Read the file and open it
# Delete the all window content but the first
# Remodel the input to be more relevant to this program
# The output should be the final window
# Based on the sample output from the website, I should create something similar

from graphics import *
from Chapter04.U04_Ex02_Archery import makeCircle
import math


def main():
    file = input("Type the file name you want to word check: ")
    f = open(file, "r")

    y = int(f.readline(1))
    win = GraphWin("Exam Graph", 600, y*100)

    y = 75
    i = 1
    lines = 0

    Text(Point(300, 20), "Exam Scores").draw(win)
    for line in f:
        if lines > 0:
            words = line.split()
            z = words
            Text(Point(100, y*i+10), z[0]).draw(win)

            score = int(z[1])
            Rectangle(Point(score*6, y*i-20), Point(170, y*i+50)).draw(win)
            i = i+1
        lines = lines + 1

    win.getMouse()
    win.close()


main()
