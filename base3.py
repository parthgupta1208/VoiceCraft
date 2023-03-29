import tkinter as tk
from PIL import Image, ImageTk
import speech_recognition as sr
import threading
import queue

class MainWindow:
    def __init__(self):
        # Initialize the Tkinter window
        self.window = tk.Tk()
        self.window.overrideredirect(True)  # Remove title bar
        self.window.geometry("+0+0")  # Set window position to top-left corner
        self.window.attributes('-alpha', 0.6)  # Set window transparency to 60%
        self.window.resizable(False, False)  # Disable resizing
        self.window.bind('<Escape>', lambda e: self.window.quit())  # Exit on pressing Esc

        # # Load and set background image
        # image = Image.open("background.jpg")
        # photo = ImageTk.PhotoImage(image)
        # self.background_label = tk.Label(self.window, image=photo)
        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a canvas to draw waveform
        self.canvas = tk.Canvas(self.window, bg="white", width=500, height=100)
        self.canvas.place(x=10, y=10)

        # Set up the speech recognition thread
        self.q = queue.Queue()
        self.stopped = False
        self.thread = threading.Thread(target=self.listen, daemon=True)
        self.thread.start()

        # Set up the GUI update loop
        self.window.after(100, self.update_gui)

    def listen(self):
        # Listen to microphone input and put the waveform data in the queue
        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            while not self.stopped:
                try:
                    audio = r.listen(source, phrase_time_limit=1)
                    waveform = audio.get_wav_data()
                    waveform = list(waveform)
                    waveform_data = []
                    for i in range(0, len(waveform), 2):
                        waveform_data.append((i/2, (waveform[i] + waveform[i+1])/2))
                    self.q.put(waveform_data)
                except sr.WaitTimeoutError:
                    pass

    def update_gui(self):
        # Get waveform data from the queue and draw it on the canvas
        while not self.q.empty():
            waveform_data = self.q.get()
            self.canvas.delete("all")
            self.canvas.create_line(waveform_data, fill="black", width=2)
        self.window.after(1, self.update_gui)

    def close(self):
        # Stop the speech recognition thread
        self.stopped = True
        self.thread.join()

if __name__ == "__main__":
    app = MainWindow()
    app.window.protocol("WM_DELETE_WINDOW", app.close)
    app.window.mainloop()
