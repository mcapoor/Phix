import pyttsx3
import speech_recognition
import pyaudio
import sphinxbase
import pocketsphinx
import os

engine = pyttsx3.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
engine.setProperty('rate', 150)

recognizer = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()

model_path = pocketsphinx.get_model_path

def speak(text):
        engine.say(text)
        engine.runAndWait()
'''
def adjust():
        with mic as source:
                recognizer.adjust_for_ambient_noise(source)

adjust()
'''
speak("Say something!")

with mic as source:
        audio = recognizer.listen_in_background(source, recognizer.recognize_google(audio))
        print(audio)
                
