from tkinter.constants import CENTER
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from wikipedia.wikipedia import languages
import tkinter as tk
import tkinter.font as tkf
import requests, json
from gnewsclient import gnewsclient
import cv2
import pyscreenshot
from pycaw.pycaw import AudioUtilities
import schedule
from youtube_search import YoutubeSearch
from pytube import YouTube
from acrcloud.recognizer import ACRCloudRecognizer
import json
import sounddevice as sd
from scipy.io.wavfile import write

client = gnewsclient.NewsClient(language='english',location='india',max_results=3)
api_key = "5995f5e32100e6a622ffb2f0d088cb02"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

def youtube(query):
    query = query.replace("search youtube for", "")
    query = query.replace("search on youtube", "")
    query = query.replace("youtube", "")
    query = query.replace(" ","+")
    webbrowser.open("https://www.youtube.com/results?search_query="+query)
    
def google(query):
    query = query.replace("google", "")
    query = query.replace("search", "")
    query = query.replace(" ","+")
    webbrowser.open("www.google.com/search?q="+query)
    
def screenshot():
    ss = pyscreenshot.grab()
    ss.show()
    ss.save("Captures\\screenshot.png")

def weather(query):
    query=query.replace("what is the weather in","")
    complete_url = base_url + "appid=" + api_key + "&q=" + query
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        weatext=(" Temperature = " +
            str(round(current_temperature-273.15)) +
            " \N{DEGREE SIGN}C\nPressure = " +
            str(current_pressure) +
            " hPa\nHumidity = " +
            str(current_humidity) +
            " Percent\nDescription = " +
            str(weather_description).title())
        speak("The Temperature in "+query+" is "+str(round(current_temperature-273.15))+"degree celsius and the weather can be described as "+str(weather_description))
    else:
        speak("City Not Found")
        
def news():
    news_list = client.get_news()
    for item in news_list:
        st = item['title'].split(' - ', 1)[0]
        speak(st)

def music():
    songs = os.listdir("Songs/")
    folder=os.getcwd()
    os.startfile(os.path.join(folder, songs[0]))
        
def download(query):
        results = YoutubeSearch(query, max_results=3).to_dict()
        linkgaana="https://www.youtube.com/watch?v="+results[0]['id']
        yt = YouTube(linkgaana)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=".")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    
def time():
    strTime = datetime.datetime.now().strftime("%H hours and %M minutes")
    speak("The Time is "+strTime)
    
def wiki(query):
    query = query.replace("wikipedia", "")
    query = query.replace("what are", "")
    query = query.replace("what is","")
    try:
        results = wikipedia.summary(query, sentences=1)
        speak(results)
    except:
        query = query.replace(" ","+")
        webbrowser.open("www.google.com/search?q="+query)
        speak("opened in webbrowser")

def calculate(query):
    query = query.replace(" ","")
    query = query.replace("calculate","")
    query = query.replace("evaluate","")
    if 'into' in query:
        query = query.replace("into","*")
    if 'by' in query:
        query = query.replace("by","/")
    try:
        result=eval(query)
    except:
        result="invalid"
    speak(result)
    
def remember(query):
    if 'what' not in query:
        query=query.replace("remember ","")
        query=query.replace("remind me","")
        fil = open("rem.txt","a")
        fil.write(query+"\n")
        fil.close()
        speak("sure i will remember that for you")
    else:
        with open('rem.txt','r') as fil:
            remtemp = fil.read()
        fil.close()
        os.remove("rem.txt")
        speak("You told me to remember "+remtemp)
        
def shutdown():
    os.system("shutdown -s")