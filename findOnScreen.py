# python code to take input via voice and take a screenshot and search that spoken element on the screen using pyautogui
# pip install pyautogui
# pip install speechrecognition
# pip install pyttsx3

import pyautogui
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    speak("What do you want to search on the screen?")
    query = takeCommand().lower()
    try:
        speak("Searching...")
        print(pyautogui.locateCenterOnScreen(query + ".png"))
    except:
        speak("Sorry, I could not find it on the screen.")

# Path: screenshot.py