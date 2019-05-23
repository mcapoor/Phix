import speech_recognition

recognizer = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()

def recieveAudio():
    # Record Audio
    with speech_recognition.Microphone() as source:
        audio = recognizer.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        data = recognizer.recognize_google(audio)
        print("You said: " + data)
    except speech_recognition.UnknownValueError:
        print("Phix could not understand audio")
    except speech_recognition.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data