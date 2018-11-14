# is_triangle.py
#
# Author: Michael Hu
# Course: Coding for OOP
# Section: A2
# Date: 14 Nov 2018
# IDE: PyCharm
#
# Assignment Info
# Trimester 1 Exam
#
# Program Description

"""
Algorithm(pseudocode)
Algorithm(pseudocode)
is_triangle:
    Takes three numbers as args, and using those three numbers,
    check to see if a triangle can be formed with the lengths using the inequalities:
        a+b>c
        a+c>b
        b+c>a
    Only one if else statement is needed, using the 'and' syntax to combine all of them into one.
        If the all three statements are true, return True
        Else, return False
main:
    Get input for three variables: a, b, c
    Wait and pull from is_triangle
        If 'flag' == 1
            print("The three sides", a, b,"and", c, "can make a triangle!"
        Else
            print("The three sides", a, b,"and", c, "cannot make a triangle!"

"""

if __name__ == '__main__':

    def main():
        a = eval(input("What is side 1?"))
        b = eval(input("What is side 2?"))
        c = eval(input("What is side 3?"))

        flag1 = is_triangle(a, b, c)
        if flag1:
            print("The three sides", a, b, "and", c, "can make a triangle!")
        else:
            print("The three sides", a, b, "and", c, "cannot make a triangle!")


    def is_triangle(a, b, c):
        # return = [a, b, c]
        if(a + b > c and
            a + c > b and
           b + c > a):
            return True
        else:
            return False



    main()
