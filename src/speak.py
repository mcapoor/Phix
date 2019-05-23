import pyttsx3

engine = pyttsx3.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
engine.setProperty('rate', 150)
def speak(text):
    engine.say(text)
    engine.runAndWait()