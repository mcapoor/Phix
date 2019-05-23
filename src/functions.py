import os
import random
import time

import blue
import music
import speak
import listen
import alarm
import phone

def phix(data):
    if "hello" in data:
        answer = ['hello', 'welcome', 'good morning', 'good evening', 'hi']
        rand = random.randint(0, 4)
        response = answer[rand]
        print(response)
        speak.speak(response)

    if "how are you" in data:
        answer = ['I am good, thank you', 'I am fine, thank you', 'I am alright, thank you', 'I am okay, thank you', 'I am wonderful, thank you']
        rand = random.randint(0, 4)
        response = answer[rand]
        print(response)
        speak.speak(response)

    if "what time" in data:
        local_time = time.asctime(time.localtime(time.time()))
        print(local_time)
        speak.speak(local_time)

    if "headphones" in data:
        blue.connect()

    if "play music" in data:
        print("Do you want to listen on your headphones?")
        speak.speak("do you want to listen on your headphones?")
       
        audio = listen.recieveAudio()
        if "yes" in audio:
            blue.connect()
            music.play()
        if "no" in audio:
            music.play()

    if "pause music" in data:
        music.pause()

    if "timer for" in data:
        alarm.play_tone(data)

    if "make a call" in data:
        print("Target Phone Number?")
        speak.speak("what is the number you want to call?")
        
        audio = listen.recieveAudio()
        
        print("Confirm?")
        speak.speak("is this the correct number?")
        verify = listen.recieveAudio()

        if "yes" in verify:
            phone.call(audio)
        
    #NOT WORKING
    '''
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        print("Locating " + location )
        speak.speak("Hold on Millin, I will show you where " + location + " is.")
        os.system("C:\Program_Files_(x86)\Google\Chrome\Application\chrome.exe https://www.google.nl/maps/place/" + location + "/&amp;")
    '''