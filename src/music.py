import os
import time

import win32api
import win32con

import speak

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def play():
    os.system(r'"C:\Users\capoo\Desktop\Spotify.lnk"')
    time.sleep(7.5)
    click(400, 570)

def pause():
    click(900, 750)
    click(400, 570)


