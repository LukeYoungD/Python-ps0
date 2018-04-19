# -*- coding: cp1252 -*-
# MIT OC - CS600 - Introduction to Computer Science and Programming
# Problem Set 0: Itroduction to Python and IDLE
# Name: Luke Young
# Collaborators: None
# Time Spent: 00:12 (hr:min)
# 2018 04 19

# Program: Entering and Printing your name
# 
# Write a program that does the following in order:
# Asks the user to enter his/her date of birth.
# Asks the user to enter his/her last name.
# Prints out the user's last name and date of birth, in that order. 

birth = ""
name = ""


birth = raw_input("Hello, enter your date of birth: ")
name  = raw_input("Now, what is your surname? ")

print(name + " " + birth)
