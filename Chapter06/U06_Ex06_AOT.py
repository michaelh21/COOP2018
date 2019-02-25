# U06_Ex06_AOT.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 29 Jan 2019
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 06
#   Source: Python Programming 
#   Chapter: 06
#
# Program Description
# This program calculates the area of a triangle from user input of it's three sides.
#
#
# Algorithm (pseudocode)
# Copy paste exercise 4.10
# Make it so that on each click, the program draws a dot.
#   I can copy paste some point drawing code from unit 4

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
    makeCircle(Point(x1, y1), 5, "black").draw(win)

    g = win.getMouse()
    x2 = g.getX()
    y2 = g.getY()
    makeCircle(Point(x2, y2), 5, "black").draw(win)

    q = win.getMouse()
    x3 = q.getX()
    y3 = q.getY()
    makeCircle(Point(x3, y3), 5, "black").draw(win)

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

