
############### - Imports - ###############

from agegen import *

from namegen import *

from addressgen import *

from nickgen import *

import time

from tkinter import *

import PySimpleGUI as sg

############### - Def Calls - ###############

# Defining the profiles name
name = nameGenerator()

# Defining the profiles age
age = ageGenerator()

# Defining the profiles adddress
addr = addrGenerator()

#Defining the profiles nickname
nick = nickGen()

# Priting the above in a sentence & Adding a disclaimer
print("DISCLAIMER: ")
time.sleep(0.5)
print("None of these credentials, addresses, names, ages or others are meant to replicate a person's actual personal credentials. Any malicious use of this project is not my responsability, this is for educational purposes only.")

# Adding time for the user to read the disclaimer
time.sleep(1)

# Actually printing the final product
finalres = f"Your name is: {name} also known as (your nickname) {nick},  you live in {addr}, and you are: {age} years old!"


print(finalres)






