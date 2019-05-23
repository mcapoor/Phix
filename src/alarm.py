import winsound 
import time
import speak

def play_tone(data):
    data = data.split(" ")
    
    duration = data[4]
    unit = data[5]
    value = duration + " " + unit

    print("Setting timer for " + value)
            
    if "hour" in unit:
        duration = duration * 3600
    if "minute" in unit:
        duration = duration * 60
        
    time.sleep(int(duration))

    speak.speak("your " + value + " timer has elapsed")
    print("Timer Finished!")

    for iter in range(4):
        winsound.Beep(440, 1000)
        time.sleep(0.1)
    