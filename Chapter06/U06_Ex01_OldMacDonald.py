# U06_Ex01_OldMacDonald.py.py
# 
# Author: Michael Hu
# Course: Coding for OOP
# Section: A3
# Date: 14 Jan 2019
# IDE: #{PRODUCT_NAME}
# 
# Assignement Info
#   Exercise: 01
#   Source: Python Programming 
#   Chapter: 06
#
# Program Description
# This program writes the Old MacDonald song with lyrics for 5 different animals.
#
#
# Algorithm (pseudocode)
# Print a line for the first line of the song, which can be repeated as the last line as well
# The middle three lines of the song are to be written out with formatted variables being inserted from a list
# The lists will consist of all animals and their corresponding sound
# The prints will loop 5 times to complete the entire song
# Each time the loop restarts, we will use the loop value i to grab the position of the animal and sounds from the lists
    # and implement them as string variables to insert from formatted printing

def main():

    animals = ["cow", "pig", "dog", "horse", "cat"]
    sound = ["moo", "oink", "bark", "neigh", "meow"]

    for i in range(5):
        animal = animals[i]
        sounds = sound[i]
        print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
        print("And on that farm he had a {0}, Ei-igh, Ee-igh, Oh!".format(animal))
        print("With a {0}, {0} here and a {0}, {0} there.".format(sounds))
        print("Here a {0}, there a {0}, everywhere a {0}, {0}.".format(sounds))
        print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
        print("\n")

main()


