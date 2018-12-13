# U04_Ex10_TriangleInfo.py.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 06 Nov 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 10
# Soource: Python Programming
# Chapter: 04
#
# Program Description
# With three click of user input, the program will draw a triangle from the points and display the perimeter and area.
#
# Algorithm(pseudocode)
# Copy the RectangleInfo code
# Change the rectangle code to a polygon code that has 3 points
# Make a new set of variables for the third point in the triangle
# The perimeter is the length formula from the line segment code, but we do it 3 times here.
# The area is math.sqrt(s(s-a)(s-b)(s-c))
# s is (a+b+c)/2
# a, b, and c are the lengths of different sides
#

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

    q = win.getMouse()
    x3 = q.getX()
    y3 = q.getY()

    shape = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    shape.setOutline("black")
    shape.setFill("white")
    shape.draw(win)

    difx = abs(x2 - x1)
    dify = abs(y2 - y1)
    difx2 = abs(x3 - x2)
    dify2 = abs(y3 - y2)
    difx3 = abs(x3 - x1)
    dify3 = abs(y3 - y1)
    length1 = round(math.sqrt(difx**2 + dify**2), 1)
    length2 = round(math.sqrt(difx2**2 + dify2**2), 1)
    length3 = round(math.sqrt(difx3**2 + dify3**2), 1)

    perimeter = round((length1+length2+length3), 2)
    Text(Point(50, 20), "Perimeter:").draw(win)
    Text(Point(130, 20), perimeter).draw(win)

    s = perimeter / 2
    Area = round((math.sqrt(s*(s-length1)*(s-length2)*(s-length3))), 2)
    Text(Point(50, 50), "Area:").draw(win)
    Text(Point(130, 50), Area).draw(win)

    win.getMouse()
    win.close()


main()