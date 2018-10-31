# U04_Ex02_Archery.py.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 29 Oct 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 02
# Soource: Python Programming
# Chapter: 4
#
# Program Description
# Draws an archery target in which the center is yellow surrounded by concentric
# rings of red, blue, black, and white. Each ring has the same width, which is
# the same as the radius of the center circle
#
# Algorithm(pseudocode)
#   Import graphics library
#   Create a Graphwin
#   Draw 5 concentric circles of increasing radius (yellow, red blue, black, white)
#       Each outer ring has a radius greater than previous, in increments equal to center circle radius
#   Draw circles from outside in
#

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