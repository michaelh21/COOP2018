# U04_Ex03_DrawFace.py.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 29 Oct 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 03
# Soource: Python Programming
# Chapter: 4
#
# Program Description
# The program will draw some sort of face. For me, I will draw a head, a nose, a mouth, and eyes.
#
# Algorithm(pseudocode)
# import graphics.py
# Create a GraphWin
# Draw circle for head
# Draw eyes
# Draw nose
# Draw mouth

from graphics import *
from Chapter04.U04_Ex02_Archery import makeCircle

def main():
    win = GraphWin("Face", 800, 800)
    drawHead(win)
    drawEyes(win)
    drawNose(win)
    drawMouth(win)
    input("press RETURN to exit.")
    win.close()

def drawHead(win):
    """
    Draw a big white circle filling up the screen; Since the window is 800x800, the radius should be 350
    :param win:
    :return:
    """
    makeCircle(Point(400, 400), 350, "white").draw(win)


def drawEyes(win):
    """
    Draw two black dots around the top portion of the face with a smaller radius
    These dots should have the same y position
    :param win:
    :return:
    """
    makeCircle(Point(600, 200), 50, "black").draw(win)
    makeCircle(Point(300, 200), 50, "black").draw(win)

def drawNose(win):
    """
    I want to make the nose red and a circle with the radius of 30
    :param win:
    :return:
    """
    makeCircle(Point(450, 280), 30, "red").draw(win)


def drawMouth(win):
    """
    I want the mouth to be massive and red, around 150 radius and somewhere leaning to the right.
    :param win:
    :return:
    """
    makeCircle(Point(500, 500), 130, "red").draw(win)


main()

