# U05_Ex01_convert_date.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 05 Dec 2018
# IDE: PyCharm
#
# Assignment Info
# Exercise: 01
# Soource: Python Programming
# Chapter: 5
#
# Program Description
#     Converts day month and year numbers into two date formats
#
# Algorithm(pseudocode)
# Copy dateconvert2.py and paste it here
# Use one input line and request all of the variable values: day, month, year
# Use the split function at the end of the input line and convert them into integers with y=int(var[x])
# Keep the months code the same
# We can delete the previous output codes and replace it with a string format output.


def main():
    all = input("Enter the day, month, and year separated by commas: ").split(",")

    day, month, year = int(all[0]), int(all[1]), int(all[2])

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monthstr = months[month - 1]

    print("The date is {0}/{1}/{2}, or, {3} {1}, {2}".format(month, day, year, monthstr))


main()
