# U04_Ex07_CircleIntersection.py.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 06 Nov 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 07
# Soource: Python Programming
# Chapter: 04
#
# Program Description
# This program will compute the intersection of a circle, and the screen will display a line that shows the information.
# The circle is also a user input, from the radius and the y intercept of the line.
# The program will also output a graph with two lines intersecting each other in the middle of the window.
# Numbers will be aligned on the two lines signifying x and y values.
#
# Algorithm(pseudocode)
# Copy over the apr entry program so most gui things are already written
# Replace all variables and text so that it is more relevant to this program
# I can delete all the output functions and replace them with the creation of a new window
# The new window will have the circle with the user input radius and the horizontal line going across the y-intercept
    # It will also include the lines and the coordinates for a graph type grid
        # Two lines down the middle of both x and y will do, and I'll use a loop for the numbers.
# I need to print out the x values of each dot anyways, so I will use the given formula for the x value of the dots.
    # The dots are always going to be on the line, so the y values will be the given y intercept.

from graphics import *
from Chapter04.U04_Ex02_Archery import makeCircle
import math

def main():
    win = GraphWin("CircleIntersection", 400, 400)
    program(win)


def program(win):
    Text(Point(180, 30), "Radius:").draw(win)
    Text(Point(180, 50), "Y-Intercept:").draw(win)

    inputText = Entry(Point(250, 30), 5)
    inputText.setText("0.0")
    inputText.draw(win)

    inputText1 = Entry(Point(250, 50), 5)
    inputText1.setText("0.0")
    inputText1.draw(win)

    button = Text(Point(200, 200), "Create")
    button.draw(win)
    Rectangle(Point(150, 150), Point(250, 250)).draw(win)

    win.getMouse()

    radius = float(inputText.getText())
    yintercept = float(inputText1.getText())

    win.getMouse()
    win.close()

    # OUTPUT
    # The new window will have the circle with the user input
    # radius and the horizontal line going across the y-intercept
    # It will also include the lines and the coordinates for a graph type grid
    # Two lines down the middle of both x and y will do, and I'll use a loop for the numbers.
    win = GraphWin("Circle", 400, 400)
    makeCircle(Point(200, 200), radius * 17.5, "yellow").draw(win)

    shape = Rectangle(Point(0, 200), Point(400, 200))
    shape.setOutline("black")
    shape.setFill("black")
    shape.draw(win)

    shape = Rectangle(Point(200, 0), Point(200, 400))
    shape.setOutline("black")
    shape.setFill("black")
    shape.draw(win)

    point = 25
    num = -10
    for i in range(11):
        Text(Point(point, 200), num).draw(win)
        Text(Point(200, point), -1 * num).draw(win)
        point = point + 35
        num = num + 2

    shape = Rectangle(Point(0, 200 - yintercept * 17.5), Point(400, 200 - yintercept * 17.5))
    shape.setOutline("aqua")
    shape.setFill("aqua")
    shape.draw(win)

    # I need to print out the x values of each dot anyways, so I will use the given formula for the x value of the dots.
    # The dots are always going to be on the line, so the y values will be the given y intercept.
    xval = round((math.sqrt((radius ** 2) - (yintercept ** 2))), 1)
    # Drawing the two dots
    makeCircle(Point(xval*17.5+200, 200 - yintercept * 17.5), 5, "red").draw(win)
    makeCircle(Point(xval*-17.5+200, 200 - yintercept * 17.5), 5, "red").draw(win)

    Text(Point(50, 20), "X Values:").draw(win)
    Text(Point(100, 20), xval).draw(win)
    Text(Point(140, 20), -1*xval).draw(win)

    win.getMouse()
    win.close()


main()
