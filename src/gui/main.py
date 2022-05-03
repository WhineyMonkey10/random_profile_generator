from asyncore import read
import time
from src.gui import *

def create(width, height, text):
    import PySimpleGUI as sg
    layout = [[sg.Text(text)]], [sg.Button("OK")]

    # Create the window
    window = sg.Window("Random Profile Generator", layout = layout, size = (width, height))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()