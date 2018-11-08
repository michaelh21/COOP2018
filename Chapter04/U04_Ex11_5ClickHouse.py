# U04_Ex11_5ClickHouse.py.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 06 Nov 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 11
# Soource: Python Programming
# Chapter: 04
#
# Program Description
# The program allows the user to click five times, which will draw a house with a door, window, frame, and roof.
#
# Algorithm(pseudocode)
# Copy the drawing portion of the rectangle code
# The door is drawn with the third click, and it needs to be 1/5 of the house width, so I will use the width/5
# The third click indicates the top of the door, so the top y value will be on the mouse detection
# The fourth click creates a window, which is half as wide as the door. I will just use 1/10 of the width of the house
# It also indicates the center of the window, so I can copy some code off of my first program.
# The fifth click indicates the roof peak, and the coordinates for the polygon creation are easy.
# (x1, y2) (x2, y2) (p.getX(), p.getY())
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

    shape = Rectangle(Point(x1, y1), Point(x2, y2))
    shape.setOutline("black")
    shape.setFill("white")
    shape.draw(win)

    width = abs(x2-x1)
    length = abs(y2-y1)

    # These are halved the supposed value because of center displacement
    widthdoor = width/10
    widthwindow = width/20

    q = win.getMouse()
    x3 = q.getX()
    y3 = q.getY()

    # Top left to bottom right
    shape = Rectangle(Point(x3-widthdoor, y3), Point(x3+widthdoor, y1))
    shape.setOutline("black")
    shape.setFill("brown")
    shape.draw(win)

    h = win.getMouse()
    # Copied from DrawingSquares program
    shape = Rectangle(Point(h.getX() + widthwindow, h.getY() + widthwindow),
                      Point(h.getX() - widthwindow, h.getY() - widthwindow))
    shape.setOutline("black")
    shape.setFill("aqua")
    shape.draw(win)

    r = win.getMouse()
    shape = Polygon(Point(x1, y2), Point(x2, y2), Point(r.getX(), r.getY()))
    shape.setOutline("black")
    shape.setFill("white")
    shape.draw(win)

    win.getMouse()
    win.close()


main()