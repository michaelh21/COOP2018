# U04_Ex09_RectangleInfo.py.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 06 Nov 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 09
# Soource: Python Programming
# Chapter: 04
#
# Program Description
# The program will allow the user to draw a rectangle with two clicks.
# After it is drawn, the program will display the perimeter and the area of the drawn rectangle.
#
# Algorithm(pseudocode)
# Copy the LineSegment program
# Change the line code to a rectangle code
# Delete most output and change the remaining to information relevant to this program
# The formula for perimeter is 2*(length+width) and Length*Width for Area
# I can replace the text with the results of these calculations.

from graphics import *
from Chapter04.U04_Ex02_Archery import makeCircle
import math

def main():
    win = GraphWin("RectangleInfo", 400, 400)
    program(win)


def program(win):
    p = win.getMouse()
    x1 = p.getX()
    y1 = p.getY()

    g = win.getMouse()
    x2 = g.getX()
    y2 = g.getY()

    shape = Rectangle(Point(x1, y1), Point(x2, y2))
    shape.setOutline("black")
    shape.setFill("white")
    shape.draw(win)

    length = abs(x2-x1)
    width = abs(y2-y1)

    perimeter = round((2*(length+width)), 2)
    Text(Point(50, 20), "Perimeter:").draw(win)
    Text(Point(130, 20), perimeter).draw(win)

    Area = round((length*width), 2)
    Text(Point(50, 50), "Area:").draw(win)
    Text(Point(130, 50), Area).draw(win)

    win.getMouse()
    win.close()


main()