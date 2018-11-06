# U04_Ex05_Dice.py.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 02 Nov 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 05
# Soource: Python Programming
# Chapter: 4
#
# Program Description
# The program will draw 5 dice in straight order
#
# Algorithm(pseudocode)
# Import needed graphics
# Create GraphWin
# Draw Background
# Draw 5 Dice
#   Draw dots

from graphics import *
from Chapter04.U04_Ex02_Archery import makeCircle

def main():
    win = GraphWin("Five Dice", 1600, 400)
    drawBackground(win)
    drawDice(win)
    drawOne(win)
    drawTwo(win)
    drawThree(win)
    drawFour(win)
    drawFive(win)
    input("press RETURN to exit.")
    win.close()

def drawBackground(win):
    """
    The background should be green. Using a rectangle that is 1600x400 would work. Make sure the outline is green also.
    :param win:
    :return:
    """
    shape = Rectangle(Point(0, 0), Point(1600, 400))
    shape.setOutline("green")
    shape.setFill("green")
    shape.draw(win)

def drawDice(win):
    """
    This section will create five white squares with black outlines. each of these squares should be 200x200.
    Each of these squares will also have a space of 50 pixels in between; Therefor each should have 250 difference.
    The y coordinates will be consistent throughout.
    :param win:
    :return:
    """
    shape1 = Rectangle(Point(50, 100), Point(250, 300))
    shape1.setOutline("black")
    shape1.setFill("white")
    shape1.draw(win)

    shape2 = Rectangle(Point(300, 100), Point(500, 300))
    shape2.setOutline("black")
    shape2.setFill("white")
    shape2.draw(win)

    shape3 = Rectangle(Point(550, 100), Point(750, 300))
    shape3.setOutline("black")
    shape3.setFill("white")
    shape3.draw(win)

    shape4 = Rectangle(Point(800, 100), Point(1000, 300))
    shape4.setOutline("black")
    shape4.setFill("white")
    shape4.draw(win)

    shape5 = Rectangle(Point(1050, 100), Point(1250, 300))
    shape5.setOutline("black")
    shape5.setFill("white")
    shape5.draw(win)

# Each of these dots should have the same size; maybe radius 10
# When copying dots over to another def, add around 250 to each x coordinate from the last
def drawOne(win):
    """
    This program will draw one black dot in the center of the first dice. My guess is (150, 200).
    :param win:
    :return:
    """
    makeCircle(Point(150, 200), 10, "black").draw(win)

def drawTwo(win):
    """
    On a normal dice, there are two dots that go diagonal to each other, with the midpoint at the center.
    I'm guessing (450, 150) & (350, 250)
    :param win:
    :return:
    """
    makeCircle(Point(350, 150), 10, "black").draw(win)
    makeCircle(Point(450, 250), 10, "black").draw(win)

def drawThree(win):
    """
    On a normal dice, there are three dots that go diagonal to each other, with one dot at the center.
    I'm guessing (700, 150), (650, 200), and (600, 250)
    :param win:
    :return:
    """
    makeCircle(Point(700, 150), 10, "black").draw(win)
    makeCircle(Point(650, 200), 10, "black").draw(win)
    makeCircle(Point(600, 250), 10, "black").draw(win)

def drawFour(win):
    """
    On a normal dice, there are four dots that are in a square formation. I'll take the two coordinates from the second
    dice and invert them to create the other two dots.

    I'm guessing (950, 150) (850, 250) (950, 250) (850, 150)
    :param win:
    :return:
    """
    makeCircle(Point(950, 150), 10, "black").draw(win)
    makeCircle(Point(850, 250), 10, "black").draw(win)
    makeCircle(Point(950, 250), 10, "black").draw(win)
    makeCircle(Point(850, 150), 10, "black").draw(win)

def drawFive(win):
    """
    On a normal dice, there are five dots that are in a square formation, but one dot is in the middle.
    I'll take the coordinates from the four dots and add a dot in the middle.

    I'm guessing (1100, 150) (1200, 250) (1200, 150) (1100, 250) (1150, 200)
    :param win:
    :return:
    """
    makeCircle(Point(1100, 150), 10, "black").draw(win)
    makeCircle(Point(1200, 250), 10, "black").draw(win)
    makeCircle(Point(1200, 150), 10, "black").draw(win)
    makeCircle(Point(1100, 250), 10, "black").draw(win)
    makeCircle(Point(1150, 200), 10, "black").draw(win)


main()
