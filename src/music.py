import os
import time

import speak
import click

def play():
    os.system(r'"C:\Users\capoo\Desktop\Spotify.lnk"')
    time.sleep(7.5)
    click.click(400, 570)

def pause():
    click.click(900, 750)
    click.click(400, 570)


