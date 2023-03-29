import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import speech_recognition as sr
import threading
import ctypes
from matplotlib.animation import FuncAnimation

# Parameters
CHUNKSIZE = 1024 # number of audio samples per frame
RATE = 44100 # sampling rate in Hz
UPDATE_INTERVAL = 20 # update interval for the plot in ms

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNKSIZE)

# Initialize plot
fig, ax = plt.subplots(facecolor='black', figsize=(3,1), dpi=100)
plt.axis('off')
line, = ax.plot(np.random.rand(CHUNKSIZE), color='red', linewidth=2)
ax.set_ylim(-1, 1)

# Function to update plot
def update_plot(frame):
    # Read audio from stream
    data = stream.read(CHUNKSIZE, exception_on_overflow=False)
    # Convert byte data to numpy array
    samples = np.frombuffer(data, dtype=np.int16)
    # Normalize samples
    samples = samples / 2**15
    # Update plot
    line.set_ydata(samples)
    return line,

# Create animation
ani = FuncAnimation(fig, update_plot, blit=True, interval=UPDATE_INTERVAL)

# Define a function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Speak now...")
            audio = r.listen(source)
            print("Processing...")
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Start a new thread for speech recognition
speech_thread = threading.Thread(target=recognize_speech)
speech_thread.start()

# Create tkinter window
root = tk.Tk()
root.overrideredirect(True)
root.geometry("300x100+{}+{}".format(ctypes.windll.user32.GetSystemMetrics(0) - 320, 20))
root.resizable(False, False)
root.attributes("-alpha", 0.6)

# Create canvas for plot
canvas = tk.Canvas(root, width=300, height=100, highlightthickness=0)
canvas.pack()

# Embed plot in canvas
plot_widget = FigureCanvasTkAgg(fig, master=canvas)
plot_widget.draw()
plot_widget.get_tk_widget().place(relx=0.5, rely=0.5, anchor="center")

# Start tkinter event loop
root.mainloop()

# Stop and close audio stream
stream.stop_stream()
stream.close()
p.terminate()
