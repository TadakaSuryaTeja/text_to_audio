import time

from gtts import gTTS
import os
import pyttsx3


def speak_gtts():
    """gTTS text to speak"""
    mytext = 'Welcome to geeksforgeeks!'
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("welcome.mp3")


def test_speak_pyttsx3():
    engine = pyttsx3.init()  # object creation

    """ RATE"""
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    print(rate)  # printing current voice rate
    engine.setProperty('rate', 175)  # setting up new voice rate

    """VOLUME"""
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    print(volume)  # printing current volume level
    engine.setProperty('volume', 0.7)  # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')  # getting details of current voice
    # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 1 for female

    engine.say("Hello World!")
    # engine.say('My current speaking rate is ' + str(rate))
    engine.runAndWait()
    engine.stop()

    # """Saving Voice to a file"""
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    # engine.save_to_file('Hello_World', 'test.mp3')
    # engine.runAndWait()


def test_voice_text_file():
    engine = pyttsx3.init(driverName='sapi5')
    engine.setProperty('rate', 175)  # setting up new voice rate
    engine.setProperty('volume', 0.9)  # setting up volume level  between 0 and 1

    infile = "sample.txt"
    f = open(infile, 'r')
    theText = f.read()
    f.close()
    time.sleep(10)
    engine.say(theText)
    engine.runAndWait()
    engine.save_to_file(theText, 'name.mp3')
    engine.runAndWait()
    engine.stop()


