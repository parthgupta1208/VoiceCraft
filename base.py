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

# #draw waveform on canvas
# def draw_waveform(audio):
#     global canvas
#     canvas.delete("all")
#     canvas.create_line(0, 50, 500, 50, fill="red")
#     for index, value in enumerate(audio.get_raw_data()):
#         if index % 2 == 0:
#             canvas.create_line(index, 50, index, 50 - value, fill="blue")
#         else:
#             canvas.create_line(index, 50, index, 50 + value, fill="blue")

#draw waveform on canvas but more beautiful
def draw_waveform(audio):
    waveform = audio.get_wav_data()
    waveform = list(waveform)
    waveform_data = []
    for i in range(0, len(waveform), 2):
        waveform_data.append((i/2, (waveform[i] + waveform[i+1])/2))
    canvas.delete("all")
    canvas.create_line(waveform_data, fill="black", width=2)

#funtion to take command from user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while True:
            try:
                audio = r.listen(source, phrase_time_limit=1)
                draw_waveform(audio)
            except sr.WaitTimeoutError:
                pass
            finally:
                break
        try:
            #print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
        except Exception as e:
            return ""
        return query

def main():
    global canvas
    root = tk.Tk()
    root.attributes('-alpha',0.6)
    root.attributes('-topmost', True)
    root.overrideredirect(1)
    root.geometry('300x150-20+20')
    root.configure(background='black')
    root.resizable(0,0)
    canvas = tk.Canvas(root, bg="white", width=500, height=100)
    canvas.place(x=10, y=10)
    root.after(100,takeCommand)
    root.mainloop()

if __name__ == "__main__":
    main()