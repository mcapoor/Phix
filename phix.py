import pyttsx3
import speech_recognition
import pyaudio
import sphinxbase
import pocketsphinx
import os
import random
import time

import blue

engine = pyttsx3.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
engine.setProperty('rate', 150)
def speak(text):
        engine.say(text)
        engine.runAndWait()

recognizer = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()
def recieveAudio():
    # Record Audio
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("What do you need?")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except speech_recognition.UnknownValueError:
        print("Phix could not understand audio")
    except speech_recognition.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def phix(data):
    if "hello" in data:
        answer = ['hello', 'welcome', 'good morning', 'good evening', 'hi']
        rand = random.randint(0, 4)
        response = answer[rand]
        print(response)
        speak(response)

    if "how are you" in data:
        answer = ['I am good, thank you', 'I am fine, thank you', 'I am alright, thank you', 'I am okay, thank you', 'I am wonderful, thank you']
        rand = random.randint(0, 4)
        response = answer[rand]
        print(response)
        speak(response)

    if "time" in data:
        local_time = time.asctime(time.localtime(time.time()))
        print(local_time)
        speak(local_time)

    if "headphones" in data:
        blue.connect()

    #NOT WORKING
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        print("Locating " + location )
        speak("Hold on Millin, I will show you where " + location + " is.")
        os.system("C:\Program_Files_(x86)\Google\Chrome\Application\chrome.exe https://www.google.nl/maps/place/" + location + "/&amp;")

   
# initialization
with mic as source:
    recognizer.adjust_for_ambient_noise(source)

speak("Hi Millinn, what can I do for you?")

while 1:
    data = recieveAudio()
    phix(data)