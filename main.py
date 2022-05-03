############### - Imports - ###############

from numpy import true_divide
from src.gens.agegen import *

from src.gens.namegen import *

from src.gens.addressgen import *

from src.gens.nickgen import *

from src.gens.allergies import *

from src.gens.favouritefood import *

from src.gens.borngen import *

from src.gens.Bestfriend import *

from src.gens.eyecolourgen import *

from src.gui.main import *

import time

from tkinter import *

import PySimpleGUI as sg

import colorama

from colorama import Back, Fore, Style

############### - Def Calls - ###############

# Defining the profiles name
name = nameGenerator()

# Defining the profiles age
age = ageGenerator()

# Defining the profiles adddress
addr = addrGenerator()

#Defining the profiles nickname
nick = nickGen()

#Defining the profiles allergy
allergie = allergiesGen()

#Defining the profiles favourite food
favfood = favouritefood()

#Defining the profiles location of birth
born = borngen()

#Definfing the profiles best friend
bestfriend = your_best_friend()

#Defining the profiles eye colour
eyecolour = eyecolourgen()

#Auto Reset
colorama.init(autoreset=True)

# Priting the above in a sentence & Adding a disclaimer
print("DISCLAIMER: ")
time.sleep(0.5)
print(Fore.RED + "None of these credentials, addresses, names, ages or others are meant to replicate a person's actual personal credentials. Any malicious use of this project is not my responsability, this is for educational purposes only.")

# Adding time for the user to read the disclaimer
time.sleep(1)

type = input("Please enter the type of profile you would like to generate (web server, gui, text): ")

# Actually printing the final product
finalres = f"{Fore.CYAN}Your name is: {name} also known as (your nickname) {nick},  you live in {addr}, and you are: {age} years old! {allergie}. {favfood}. You were born in: {born} and your BFF is {bestfriend}. Your eye colour is: {eyecolour}"
finalguicompatible = f"Your name is: {name} also known as (your nickname) {nick},  you live in {addr}, and you are: {age} years old! {allergie}. {favfood}. You were born in: {born} and your BFF is {bestfriend}. Your eye colour is: {eyecolour}"

print(finalres)


#input("Do you want to save this profile? (Yes or No)")


#Initialise the GUI
height = 500 #2
width = 2000 #1
create(width, height, finalres)