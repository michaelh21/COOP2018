# U07_Ex16_ArcheryScore.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 01 Mar 2019
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 16
#   Source: Python Programming 
#   Chapter: 07
#
# Program Description
# This program draws an archery target, accepts five clicks as the arrow shots, and outputs the soore.
#
#
# Algorithm (pseudocode)
# Paste the 4.2 code
# Make each click draw a circle
# Make a series of if statements that check to see which circle the point is in.

from graphics import *


def main(winSide):
    win = GraphWin("Target", winSide, winSide)
    radius = win.getWidth()/12
    center = Point(win.getWidth()/2, win.getHeight()/2)
    circles = [makeCircle(center, radius * 5, "white"),
               makeCircle(center, radius * 4, "black"),
               makeCircle(center, radius * 3, "blue"),
               makeCircle(center, radius * 2, "red"),
               makeCircle(center, radius, "yellow")]

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

    p = win.getMouse()
    x4 = p.getX()
    y4 = p.getY()
    makeCircle(Point(x4, y4), 5, "black").draw(win)

    g = win.getMouse()
    x5 = g.getX()
    y5 = g.getY()
    makeCircle(Point(x5, y5), 5, "black").draw(win)



    for circle in circles:
        circle.draw(win)

def makeCircle(c, r, color):
    """
    Creates a circle object centered at c with radius r and filled with color
    :param c: Point -> center point of circle
    :param r: int -> radius of circle
    :param color: str -> color for fill
    :return: Circle -> circle object
    """
    circ = Circle(c, r)
    circ.setOutline("black")
    circ.setFill(color)
    return circ


if __name__ == '__main__':
    main(600)
    input("Press Enter to close graphics window.")