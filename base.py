import pyttsx3
import speech_recognition as sr
import tkinter as tk

#define engine for speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#function for speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#funtion to take command from user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        #print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return ""
    return query

def main():
    root = tk.Tk()
    root.title("Voice Assistant")
    root.geometry("400x400")
    root.resizable(0, 0)

    frame = tk.Frame(root)
    frame.pack()

    label = tk.Label(frame, text="Voice Assistant", font=("Arial", 20))
    label.pack()

    button = tk.Button(frame, text="Speak", font=("Arial", 20), command=lambda: speak(takeCommand()))
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()