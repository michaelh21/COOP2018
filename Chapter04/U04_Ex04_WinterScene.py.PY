# U04_Ex04_WinterScene.py.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 31 Oct 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 04
# Soource: Python Programming
# Chapter: 4
#
# Program Description
# The program will draw a snowman and a christmas tree in the winter
#
# Algorithm(pseudocode)
# Import needed graphics
# Create GraphWin
# Draw Background
#   Draw Sky
# Draw snowman
#   Draw arms
#   Draw Body
#   Draw Eyes
#   Draw Nose
#   Draw Mouth
# Draw tree

from graphics import *
from Chapter04.U04_Ex02_Archery import makeCircle

def main():
    win = GraphWin("Winter Scene", 1000, 600)
    drawSky(win)
    drawArm(win)
    drawBody(win)
    drawEyes(win)
    drawNose(win)
    drawMouth(win)
    drawTree(win)
    input("press RETURN to exit.")
    win.close()


def drawSky(win):
    shape = Rectangle(Point(0, 250), Point(1000, 0))
    shape.setOutline("black")
    shape.setFill("aqua")
    shape.draw(win)

def drawArm(win):
    shape = Rectangle(Point(350, 200), Point(650, 190))
    shape.setOutline("brown")
    shape.setFill("brown")
    shape.draw(win)


def drawBody(win):
    makeCircle(Point(500, 300), 80, "white").draw(win)
    makeCircle(Point(500, 220), 70, "white").draw(win)
    makeCircle(Point(500, 150), 50, "white").draw(win)


def drawEyes(win):
    makeCircle(Point(480, 130), 5, "black").draw(win)
    makeCircle(Point(520, 130), 5, "black").draw(win)

def drawNose(win):
    makeCircle(Point(500, 150), 5, "orange").draw(win)


def drawMouth(win):
    makeCircle(Point(480, 170), 5, "black").draw(win)
    makeCircle(Point(520, 170), 5, "black").draw(win)
    makeCircle(Point(490, 180), 5, "black").draw(win)
    makeCircle(Point(510, 180), 5, "black").draw(win)

def drawTree(win):
    shape = Rectangle(Point(200, 450), Point(220, 400))
    shape.setOutline("black")
    shape.setFill("brown")
    shape.draw(win)

    triangle = Polygon(Point(150, 400), Point(270, 400), Point(210, 300))
    triangle.setOutline("black")
    triangle.setFill("green")
    triangle.draw(win)

    triangle = Polygon(Point(160, 350), Point(260, 350), Point(210, 270))
    triangle.setOutline("black")
    triangle.setFill("green")
    triangle.draw(win)

    triangle = Polygon(Point(170, 310), Point(250, 310), Point(210, 250))
    triangle.setOutline("black")
    triangle.setFill("green")
    triangle.draw(win)

main()