#Q.1- Write a python code to find a valid email address from a text.

import re

emailadd = input("Email of the USER :- ")

m = re.search('^[a-zA-Z][a-zA-Z0-9]*[@](gmail.com|yahoo.com)', emailadd)

if m != None:
    print('Email Verified!')
else:
    print('Invalid Email Address!')

#Q.2- Write a python program to find a valid Indian phone number from a text.(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )

import re

check = input("Enter a Phone Number (Eg. +91-0123456789): ")

m = re.search('^[+][9][1][-][6-9][\d]{9}', check)

if m!= None:
    print("This was a Valid Phone Number.")
else:
    print("This was an Invalid Phone Number.")
