import time
import colorama
from colorama import Back, Fore, Style
from tkinter import *
import PySimpleGUI as sg
from numpy import true_divide

from src.globals.classes.gens import Gens

gens = Gens()

from src.gui import *
from src.gui.main import *


def gen_result(include_middle_name: str, final_type: str = "web"):
    x = 0
    name = gens.nameGenerator(include_middle_name)
    age = gens.ageGenerator()
    addr = gens.addrGenerator()
    nick = gens.nickGen()
    allergie = gens.allergiesGen()
    favfood = gens.favouritefood()
    born = gens.borngen()
    bestfriend = gens.your_best_friend()
    eyecolour = gens.eyecolourgen()
    # Initialising the final product

    finalres = f"{Fore.CYAN}Your name is {name} your nickname is {nick},  you live in {addr}, and you are {age} years old. {allergie}. {favfood}. You were born in {born} and your BFF is {bestfriend}. Your eye colour is {eyecolour}"
    webcomp = f"Your name is {name} your nickname is {nick},  you live in {addr}, and you are {age} years old. {allergie}. {favfood}. You were born in {born} and your BFF is {bestfriend}. Your eye colour is {eyecolour}"

    if final_type == "text":
        return finalres

    if final_type == "web":
        return webcomp.strip()

    if final_type == "gui":
        guicomp = f"Your name is {name} your nickname is {nick},  you live in {addr}, and you are {age} years old. {allergie}. {favfood}. You were born in {born} and your BFF is {bestfriend}. Your eye colour is {eyecolour}"
        return guicomp.strip()


def web_server(debug: bool = False):
    from flask import Flask, render_template, Response, request, redirect, url_for
    from os import getcwd

    main = Flask(__name__)
    main.template_folder = getcwd() + '/src/localserver/website/pages'
    main.static_folder = getcwd() + '/src/localserver/website/static'
    main.static_url_path = '/static'

    if debug:
        main.config['DEBUG'] = True

    @main.route('/', methods=['GET', 'POST'])
    def index():
        render = "index.html"
        return render_template(render)

    @main.route('/generate', methods=['GET', 'POST'])
    def generate():
        if request.method == "GET":
            return redirect(url_for("index"))

        render = "generation.html"
        middle_name = "No"
        if "middle_name" in request.form:
            middle_name = "Yes"

        return render_template(render, variable=gen_result(middle_name, "web"))

    return main


def process():
    # Auto Reset
    colorama.init(autoreset=True)

    # Priting the above in a sentence & Adding a disclaimer
    print("DISCLAIMER: ")
    time.sleep(0.5)
    print(
        Fore.RED + "None of these credentials, addresses, names, ages or others are meant to replicate a person's actual personal credentials. Any malicious use of this project is not my responsability, this is for educational purposes only.")

    # Adding time for the user to read the disclaimer
    time.sleep(1)

    type = input(
        f"{Fore.CYAN}Please enter the type of profile you would like to generate (web server, gui, text) web server is recommended: ")
    type = (type.casefold())

    # Using the users inpit method to determine the 'type' of profile they want to generate

    if type == "gui":
        sg.theme('BlueMono')
        middle_name = input(f"{colorama.Fore.CYAN}Do you want your name to include a middle name? (Yes or No?): ")

        print("""
    Please note that the GUI is still in development, please see the folder src/gui/ for the current gui process. 
    Although, it still works. It has been opened.
            """)
        # Initialise the GUI
        height = 500  # 2
        width = 2000  # 1
        create(width, height, gen_result(middle_name, "gui"))

    elif type == "text":
        middle_name = input(f"{colorama.Fore.CYAN}Do you want your name to include a middle name? (Yes or No?): ")
        print(gen_result(middle_name, "text"))

    elif type == "web server":
        print(f"{Fore.GREEN}Please visit http://localhost:5000/ OR http://127.0.0.1:5000")
        server = web_server()
        server.run()

    return


process()
