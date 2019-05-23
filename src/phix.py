#BASE IMPORTS
import speech_recognition
import pyaudio
import sphinxbase, pocketsphinx
import os

#MY PACKAGES
import speak
import functions
import listen

# initialization
with listen.mic as source:
    listen.recognizer.adjust_for_ambient_noise(source)

speak.speak("Hi Millinn, what can I do for you?")

while 1:
    print("How can I help?")
    data = listen.recieveAudio()
    functions.phix(data)