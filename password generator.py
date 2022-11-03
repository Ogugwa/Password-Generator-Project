import random
from random import randint
#1. Creating an empty varaible to store the password in
password_generator= ''
#2.Since the code would run multiple times we would need to create a for loop
for i in range(10):
     i= chr(randint(25,99))
     for j in range(10):
          j=chr(randint(25,99)).lower()
     password_generator= str(password_generator)+ i +j
   print( "Your password is : " + password_generator)
#3.The range signifies the number of time we want the code to select a character from
# the range of values from 25 to 99
# The chr is a module in python just like str and int;it makes it easy for the random integer to include Alphabets and Special characters in the code
