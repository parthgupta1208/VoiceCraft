#importing libraries
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests
import json

#function to check string
def check_text(query):
    
    # code to execute youtube search for the query
    if 'youtube' in query:
        query = query.replace("search youtube for", "")
        query = query.replace("search on youtube", "")
        query = query.replace("youtube", "")
        query = query.replace(" ","+")
        webbrowser.open("https://www.youtube.com/results?search_query="+query)
        speak("These are some results")
        
    # code to execute google search for the query
    elif 'google' in query or 'search' in query:
        query = query.replace("google", "")
        query = query.replace("search", "")
        query = query.replace(" ","+")
        webbrowser.open("www.google.com/search?q="+query)
        w.config(text = "Results are Shown in Browser")
        w.update()
        speak("These are some results")

    # code to capture selfie    
    elif 'capture' in query or 'selfie' in query:
        w.config(text = "Say Cheese, Hit Spacebar & Tell The Filename")
        w.update()
        speak("Say cheese, hit spacebar and tell the filename")
        captureselfie.cap()
        setevery("Photo Saved Succesfully")
        
    # code to take screenshot
    elif 'screenshot' in query:
        setevery("Taking Screenshot")
        ss = pyscreenshot.grab()
        ss.show()
        setevery("Provide Filename")
        filename=takeCommandMeowAgain().title()
        os.chdir("FridayAI\Captures")
        ss.save(filename+".png")
        setevery("Screenshot Saved Succesfully")

    # code to enable disable dnd
    elif 'dnd' in query:
        if 'enable' in query or 'on' in query:
            mutevalue=1
        if 'disable' in query or 'off' in query:
            mutevalue=0
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session.SimpleAudioVolume
            volume.SetMute(mutevalue, None)
            setevery("DND Status Set Succesfully")
    
    #code to tell weather
    elif 'what is the weather in' in query:
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
            w.config(text=weatext)
            w.update()
            speak("The Temperature in "+query+" is "+str(round(current_temperature-273.15))+"degree celsius and the weather can be described as "+str(weather_description))
        else:
            w.config(text = 'City Not Found')
            w.update()
            speak("City Not Found")

    #code to tell news   
    elif 'news' in query:
        news_list = client.get_news()
        for item in news_list:
            st = item['title'].split(' - ', 1)[0]
            w.config(text = st)
            w.update()
            speak(st)

    #code to play music
    elif 'play' in query and ('music' in query or 'songs' in query or 'song' in query):
        folder="FridayAI\Songs"
        os.chdir(folder)
        setevery("Do You Want To Play Existing Songs or Download New Ones")
        query=takeCommandMeowAgain()
        if 'download' in query:
            setevery("Which Song Would You Like To Download")
            query=takeCommandMeowAgain()
            results = YoutubeSearch(query, max_results=3).to_dict()
            setevery("Choose One of The Following")
            for res in results:
                setevery(res['title'])
            query=takeCommandMeowAgain()
            if "second" in query:
                gaanano=1
            elif "third" in query:
                gaanano=2
            else:
                gaanano=0
            linkgaana="https://www.youtube.com/watch?v="+results[gaanano]['id']
            yt = YouTube(linkgaana)
            video = yt.streams.filter(only_audio=True).first()
            out_file = video.download(output_path=".")
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            setevery("Succesfully Downloaded")
            w.config(text = 'Playing '+results[gaanano]['title'])
            w.update()
            speak("Playing Music")
            os.startfile(os.path.join(folder, new_file))
        else:
            songs = os.listdir(folder)
            w.config(text = 'Playing '+songs[0])
            w.update()
            speak("Playing Music")
            os.startfile(os.path.join(folder, songs[0]))
            
    elif 'download' in query and 'song' in query:
            setevery("Which Song Would You Like To Download")
            queryx=takeCommandMeowAgain()
            results = YoutubeSearch(queryx, max_results=3).to_dict()
            setevery("Choose One of The Following")
            for res in results:
                setevery(res['title'])
            queryx=takeCommandMeowAgain()
            if "second" in queryx:
                gaanano=1
            elif "third" in queryx:
                gaanano=2
            else:
                gaanano=0
            linkgaana="https://www.youtube.com/watch?v="+results[gaanano]['id']
            yt = YouTube(linkgaana)
            video = yt.streams.filter(only_audio=True).first()
            out_file = video.download(output_path=".")
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            setevery("Succesfully Downloaded")
            setevery("Would you like to Play this Song ?")
            queryx=takeCommandMeowAgain()
            if "yes" in queryx:
                w.config(text = 'Playing '+results[gaanano]['title'])
                w.update()
                speak('Playing '+results[gaanano]['title'])
                os.startfile(os.path.join(folder, new_file))
            else:
                setevery("Okay")

    #code to recognise song        
    elif 'recognise' in query and 'song' in query:
        fs = 44100
        seconds = 10
        songrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        setevery("Sure, Listening")
        sd.wait()
        speak("Recognising")
        write('tempsongforrec.wav', fs, songrecording)
        songrecstring=acrcloud.recognize_by_file('tempsongforrec.wav', 0)
        songrecjson = json.loads(songrecstring)
        if songrecjson['status']['msg'] == 'Success' and songrecjson['metadata'] and songrecjson['metadata']['music'][0]:
            setevery("The Name of the Song is "+(songrecjson["metadata"]["music"][0]["title"])+" from the Album "+(songrecjson["metadata"]["music"][0]["album"]["name"]))
            setevery("Would you Like to Download This Song ?")
            queryx=takeCommandMeowAgain()
            queryx=queryx.lower()
            print(queryx)
            if ('download' in queryx) or ('yes' in queryx):
                folder="C:\Everything\FRIDAY\Songs"
                os.chdir(folder)
                results = YoutubeSearch((songrecjson["metadata"]["music"][0]["title"]), max_results=1).to_dict()
                gaanano=0
                linkgaana="https://www.youtube.com/watch?v="+results[gaanano]['id']
                yt = YouTube(linkgaana)
                video = yt.streams.filter(only_audio=True).first()
                out_file = video.download(output_path=".")
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                setevery("Succesfully Downloaded")
            else:
                setevery("Okay")
        else:
            setevery("Sorry, Could Not Recognise")
        print(songrecjson)
        
    # code to suggest
    elif 'suggest' in query:
        query = query.replace("suggest", "best")
        query = query.replace(" ","+")
        webbrowser.open("www.google.com/search?q="+query)
        w.config(text = "Results are Shown in Browser")
        w.update()
        speak("These are some results")
        
    #code to tell time
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H hours and %M minutes")
        w.config(text = 'The Time is '+strTime)
        w.update()
        speak("The Time is "+strTime)
    
    #code to search wikipedia
    elif 'wikipedia' in query or 'what are' in query or 'what is' in query:
        query = query.replace("wikipedia", "")
        query = query.replace("what are", "")
        query = query.replace("what is","")
        try:
            results = wikipedia.summary(query, sentences=1)
        except:
            query = query.replace(" ","+")
            webbrowser.open("www.google.com/search?q="+query)
            w.config(text = "Results are Shown in Browser")
            w.update()
            speak("These are some results")
        else:
            w.config(text = 'According to Wikipedia '+results)
            w.update()
            speak("According to Wikipedia"+results)

    #code to calculate
    elif 'calculate' in query or 'evaluate' in query:
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
        w.config(text = "Results is "+str(result))
        w.update()
        speak("Result is "+str(result))
        
    #code to remember
    elif 'remember' in query or 'remind' in query:
        if 'what' not in query:
            query=query.replace("remember ","")
            query=query.replace("remind me","")
            fil = open("rem.txt","a")
            w.config(text = "Okay")
            w.update()
            speak("Okay")
            fil.write(query+"\n")
            fil.close()
        else:
            with open('rem.txt','r') as fil:
                remtemp = fil.read()
            w.config(text = "You Told Me To Remember : \n"+remtemp.title())
            w.update()
            speak("You told me to remember "+remtemp)
            fil.close()
            os.remove("rem.txt")
    
    #code to open apps
    elif 'run' in query:
        query=query.replace("run ","")
        try:
            w.config(text = "Opening "+query)
            w.update()
            speak("Opening "+query)
            if (os.system(query))==1:
                w.config(text = "Could Not Open")
                w.update()
                speak("Could not open")
        except:
            w.config(text = "Could Not Open")
            w.update()
            speak("Could not open")
            
    #code to shutdown
    elif 'shutdown' in query:
        w.config(text = 'Shutting Down')
        w.update()
        speak("Shutting Down")
        os.system("shutdown -s")            

    #code to exit
    elif 'bye' in query or 'exit' in query:
        w.config(text = 'Bella Ciao')
        w.update()
        speak("Bella Ciao")
        root.destroy()
        exit(0)
    
    else:
        query = query.replace(" ","+")
        webbrowser.open("www.google.com/search?q="+query)
        w.config(text = "Results are Shown in Browser")
        w.update()
        speak("These are some results")

#code to run the main function
if __name__ == "__main__":
    main()
    root.mainloop()