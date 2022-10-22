import pywhatkit as pwk
import subprocess
import datetime
import pandas as pd
import os
import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 210)

def play_music(song):
    pwk.playonyt(song)



def shutdown():
    subprocess.call(["shutdown", "-f", "-s", "-t", "60"])


def restart():
    subprocess.call(["shutdown", "-f", "-r", "-t", "60"])


def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


def open(app):
    directory = os.getcwd()
    directory = directory.replace('\\', '/')
    setup = pd.read_csv(rf"{directory}/helpers/setup_application.txt", sep='=', index_col=0, squeeze=True, header=None)
    app = setup[app]
    # launch application
    os.startfile(f'"{app}"')


def search(q):
    pwk.search(q)


def time():
    speak(f'The time is {datetime.datetime.now().strftime("%I:%M %p")}')


def speak(reply):
    engine.say(reply)
    engine.runAndWait()
