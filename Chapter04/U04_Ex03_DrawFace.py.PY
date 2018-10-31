# U04_Ex03_DrawFace.py.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 29 Oct 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 
# Soource: Python Programming
# Chapter: 
#
# Program Description
# Draws a face
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
    makeCircle(Point(400, 400), 350, "yellow").draw(win)


def drawEyes(win):
    makeCircle(Point(600, 200), 50, "black").draw(win)
    makeCircle(Point(300, 200), 50, "black").draw(win)

def drawNose(win):
    makeCircle(Point(450, 280), 30, "red").draw(win)


def drawMouth(win):
    makeCircle(Point(500, 500), 130, "red").draw(win)


main()

