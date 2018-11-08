# U04_Ex08_LineSegment.py.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 06 Nov 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 
# Soource: Python Programming
# Chapter: 
#
# Program Description
# The user is allowed to draw a line segment, and then the program displays information about the line segment.
# The information contains the midpoint of the segment, the length of the line, and the slope of it as well.
#
# Algorithm(pseudocode)
# I'm going to copy some code off of the first exercise of this unit, getting all the imports I need.
# The lines I'm going to copy are the mouse detection point code lines.
# I make those lines the first in the program, then use the result of each click to transfer them into ints.
# Using the final four ints, I can plug it into a line code.
# To find the midpoint of the line I can just take the two coordinate values and average them to get the middle point
# To print the length, I need to use the formula from the unit book, which is math.sqrt(dx**2 + dy**2)
# To print the slope, I can use the formula dy/dx

from graphics import *
from Chapter04.U04_Ex02_Archery import makeCircle
import math

def main():
    win = GraphWin("LineSegment", 400, 400)
    program(win)


def program(win):
    p = win.getMouse()
    x1 = p.getX()
    y1 = p.getY()

    g = win.getMouse()
    x2 = g.getX()
    y2 = g.getY()

    aLine = Line(Point(x1, y1), Point(x2, y2))
    aLine.draw(win)

    xaverage = (x2 + x1) / 2
    yaverage = (y2 + y1) / 2
    makeCircle(Point(xaverage, yaverage), 5, "aqua").draw(win)\

    difx = x2 - x1
    dify = y2 - y1
    length = round(math.sqrt(difx**2 + dify**2), 1)
    Text(Point(50, 20), "Length:").draw(win)
    Text(Point(100, 20), length).draw(win)

    slope = round((dify / difx), 2)
    Text(Point(50, 50), "Slope:").draw(win)
    Text(Point(100, 50), slope).draw(win)

    win.getMouse()
    win.close()


main()
