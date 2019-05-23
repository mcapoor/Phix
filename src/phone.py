import webbrowser
import time
import pyperclip
import pyautogui

import speak
import click

def call(audio):
    pyperclip.copy(audio)

    

    page = webbrowser.open_new("https://voice.google.com/u/0/calls")
    print(page)

    time.sleep(8)
    click.click(150, 250)
    time.sleep(1)
    click.click(750, 250)
    time.sleep(1)

    pyperclip.paste()
    pyautogui.hotkey('ctrl', 'v', 'enter', interval = 0.15)
