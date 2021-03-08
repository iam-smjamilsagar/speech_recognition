# python speech recognition
# pip install SpeechRecognition

# python text to speech
# pip install pyttsx3

# python audio
# pip install PyAudio

# search in youtube
# pip install pywhatkit

# collects parse data from Wikipedia
# pip install wikipedia

# One line jokes for programmers
# pip install pyjokes

# This Python package is meant to scrape and parse Google, Google Scholar, Bing, Baidu, Yandex, Yahoo, Ebay results using SerpApi.
# pip install google-search-results

# we have to install all these files in the terminal

import speech_recognition as sr
# here we have to import the speech recognition as sr in short form

import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes


listener = sr.Recognizer()
alexa = pyttsx3.init()

# by default it'll talk as a male. if we want to change the voice like women then check below
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)
# Actually google voice has two types of voice. One is for male and another is for female. Here 0 id is for male and 1 is for female.

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():

    try:
        with sr.Microphone() as source:
# sr means speech recognition, will connect our device microphone which we've called here source
            print('Your device is listening, Please speak...')
    # to read the voice, we can listen through the listener
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
    # to convert audio to txt we need google api
            command = command.lower()
    # it will show all the commands in lowercase
            if 'alexa' in command:
    # if alexa is available in a command that time it will show the result otherwise not
                command = command.replace('alexa', '')
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is: ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        # if we want to play the song on youtube(playonyt)

    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'date' in command:
        print(command)
        talk('Sorry brother, I am in another relationship. Try it with another guy.')
    else:
        talk('Did not get it. Can you please tell it again')
        pywhatkit.search(command)
# if the machine doesn't get any related command that time it will search on google engine

# while True:
run_alexa()