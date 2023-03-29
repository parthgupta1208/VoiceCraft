import tkinter as tk
from PIL import Image, ImageTk
import speech_recognition as sr

class MainWindow:
    def __init__(self):
        # Initialize the Tkinter window
        self.window = tk.Tk()
        self.window.overrideredirect(True)  # Remove title bar
        self.window.geometry("300x150-20+20")  # Set window position to top-left corner
        self.window.attributes('-alpha', 0.6)  # Set window transparency to 60%
        # self.window.resizable(False, False)  # Disable resizing
        self.window.bind('<Escape>', lambda e: self.window.quit())  # Exit on pressing Esc

        # Load and set background image
        # image = Image.open("background.jpg")
        # photo = ImageTk.PhotoImage(image)
        # self.background_label = tk.Label(self.window, image=photo)
        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a canvas to draw waveform
        self.canvas = tk.Canvas(self.window, bg="white", width=200, height=100)
        self.canvas.place(x=10, y=10)

        # Start the microphone and recognize speech
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        self.listen()

    def listen(self):
        # Listen to microphone input and display waveform
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            while True:
                try:
                    audio = self.r.listen(source, phrase_time_limit=1)
                    self.draw_waveform(audio)
                except sr.WaitTimeoutError:
                    pass

    def draw_waveform(self, audio):
        # Draw waveform on the canvas
        waveform = audio.get_wav_data()
        waveform = list(waveform)
        waveform_data = []
        for i in range(0, len(waveform), 2):
            waveform_data.append((i/2, (waveform[i] + waveform[i+1])/2))
        self.canvas.delete("all")
        self.canvas.create_line(waveform_data, fill="black", width=2)

if __name__ == "__main__":
    MainWindow().window.mainloop()
