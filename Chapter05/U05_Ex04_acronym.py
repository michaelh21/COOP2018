# U05_Ex04_acronym.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 07 Dec 2018
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 4
#   Source: Python Programming 
#   Chapter: 05
#
# Program Description
# This program takes a phrase as input and makes an acronym out of the phrase.
#
#
# Algorithm (pseudocode)
# The split function will most likely be used in this program
# Get the input and split it up
# Create a variable to be used as the true acronym that we can add to
# Create a loop that grabs the first word in every word and adds to the variable we created
# Capitalize the true acronym using the .upper function and assign another variable the capital value
# Print that variable


def main():
    acronym = input("Enter the phrase your would like to convert to an acronym: ")

    list = acronym.split(' ')

    acro = ""

    for word in list:
        acro += word[0]

    acroup = acro.upper()

    print("The acronym is: {0}.".format(acroup))

main()
