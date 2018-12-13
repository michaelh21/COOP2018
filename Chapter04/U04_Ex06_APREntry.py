# U04_Ex06_APREntry.py.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 06 Nov 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 06
# Source: Python Programming
# Chapter: 04
#
# Program Description
# The program will refactor the APR program so that the input is graphical through entry points. The output is also
# in the same graphical window, and will display somewhere else on the screen as soon as the user clicks "calculate."
#
# Algorithm(pseudocode)
# Copy the convert_gui.pyw program over
# Trash the setCoords; Replace all coordinates with actual coordinates relative to window size.
# For this program, it requires two inputs, so I will copy the input code and lower the y values by 20.
# I'll replace the names of every variable to make it more relevant to the program
# I'll duplicate the input code over to the variables principal and APR
# Copy the future value equation over with the for loop that runs for 10 times
# The bottom text will display the end result of the for loop

from graphics import *


def main():
    win = GraphWin("APREntry", 400, 400)

    Text(Point(180, 30), "Principal:").draw(win)
    Text(Point(180, 50), " APR:").draw(win)

    inputText = Entry(Point(250, 30), 5)
    inputText.setText("0.0")
    inputText.draw(win)

    inputText1 = Entry(Point(250, 50), 5)
    inputText1.setText("0.0")
    inputText1.draw(win)

    outputText = Text(Point(200, 350), "")
    outputText.draw(win)

    button = Text(Point(200, 200), "Calculate")
    button.draw(win)
    Rectangle(Point(150, 150), Point(250, 250)).draw(win)

    win.getMouse()

    principal = float(inputText.getText())
    APR = float(inputText1.getText())

    for i in range(10):
        principal = principal * (1+APR)

    outputText.setText(round(principal, 2))
    button.setText("Quit")

    win.getMouse()
    win.close()


main()
