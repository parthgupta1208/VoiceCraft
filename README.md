# Voice Craft - Desktop Help AI Assistance for People with Disabilities

Voice Craft is a desktop AI assistance tool designed to help people with disabilities operate a computer using their voice. The tool requires users to set up OpenAI Secret Key and OpenWeatherMap API Key, as well as install various libraries and dependencies.

## Features

Voice Craft can perform a range of tasks, including:

- **Browser and OS Operations**: Voice Craft can operate the web browser and perform tasks if the user starts their sentence with "Friday open chrome..." or "Friday open...". It can also reply to general queries starting with "Friday...".

- **Typing Mode**: Users can activate typing mode by saying "activate type", and all their spoken words will be typed with proper punctuation.

- **Mouse Mode**: Users can activate mouse mode by saying "activate voice mouse", and all their spoken words will be used to control the mouse.

- **Coding Mode**: Users can activate coding mode by saying "activate code", and Voice Craft can generate code in a specific programming language. The program will open in VSCode and start running.

- **Other Features**: Voice Craft can perform various other tasks, including YouTube and Google searches, taking screenshots, providing weather updates, downloading files, playing music, telling the time, remembering things, opening apps, shutting down the computer, and more. 

## Requirements

In order to use Voice Craft, you must have:

- OpenAI Secret Key
- OpenWeatherMap API Key
- Various Python libraries, including:
  - Pyaudio
  - Numpy
  - Matplotlib
  - Speech Recognition
  - Threading
  - Pyttsx3
  - Deepmultilingualpunctuation
  - Pyautogui
  - Requests
  - Wikipedia
  - Webbrowser
  - Os
  - Friday
  - Gnewsclient
- Tkinter and Matplotlib for the GUI

## Usage

To use Voice Craft, first clone the repository using the following command:

`git clone https://github.com/parthgupta1208/VoiceCraft.git`

Now, simply run `python v3.py` and speak commands into the microphone. 

To activate specific modes or tasks, use the appropriate trigger phrases:

- "Activate type" for typing mode
- "Activate voice mouse" for mouse mode
- "Activate code" for coding mode

For other tasks, simply start your sentence with the appropriate keyword, such as "YouTube search", "Google search", "Screenshot", "News", "Weather", "Download", "Music", "Time", "Wikipedia search", "Calculate", "Remember", "Open app", or "Shutdown".

## Credits

Voice Craft was created by Parth Gupta using the GPT-3.5-turbo model from OpenAI, along with various other Python libraries and APIs. The tool was designed to help people with disabilities operate a computer with ease and efficiency. 

## License

Voice Craft is licensed under the MIT License. Please see the `LICENSE` file for more information.

## Support

For help with Voice Craft, please contact the developers or refer to the documentation provided with the application.