# U04_Ex01_descriptive_name.py.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 23 Oct 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 01
# Soource: Python Programming
# Chapter: 4
#
# Program Description
# Replace the draw circle program with squares and have each new position be a new square
# and print a message at the end of the loop to close to program with the next click
#
# Algorithm(pseudocode)
# Import Graphics
# Import Circle program
# Change the shape variable from circle to square parameters with points being couples
# Instead of clicks moving the square, clicks will create new ones using the previous code to create the first square
# This is done by using the square creation text, copy pasted into the loop
# Change the square's center to the mouse location, which is done by
# adding 15 and subtracting 15 from the top and bottom corner
# Before executing win.close(), have the user input a click with the message "Click again to quit" using Text()


# Import Graphics
from graphics import *

# Import Circle program
def main():
    win = GraphWin()

    # Change the shape variable from circle to rectangle parameters with points being couples
    shape = Rectangle(Point(50, 50), Point(20, 20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # Instead of clicks moving the square, clicks will create new
    # ones using the previous code to create the first square
    for i in range(10):
        p = win.getMouse()

        # This is done by using the square creation text, copy pasted into the loop
        # Change the square's center to the mouse location, which is done by
        # adding 15 and subtracting 15 from the top and bottom corner
        shape = Rectangle(Point(p.getX()+15, p.getY()+15), Point(p.getX()-15, p.getY()-15))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    # Before executing win.close(), have the user input a click with the message "Click again to quit" using Text()
    Text(Point(100, 100), "Click again to quit").draw(win)
    p = win.getMouse()
    win.close()


main()

