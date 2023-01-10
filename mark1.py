#required modules

import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import random

moon = pyttsx3.init('sapi5')
voices = moon.getProperty('voices')
moon.setProperty('voice', voices[0].id)

#defining functions

def speak(audio):
    moon.say(audio)
    moon.runAndWait()

def Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n") 
    except Exception:
        print("Say that again please...") 
        return 
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   
    else:
        speak("Good Evening sir!")  
    speak("How can the Moon help you?") 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gammusicrew@gmail.com', '**********')
    server.sendmail('madhavampire@gmail.com', to, content)
    server.close()


#main body of the code

if __name__=="__main__" :

    wishMe()

    while True:
        query = Command().lower()

        if 'wikipedia' in query or 'what is' in query or 'who is' in query or 'define' in query or 'defination' in query or 'meaning' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            song = random.choice(songs) 
            print(f"playing {song}...")
            os.startfile(os.path.join(music_dir, song))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            print(strTime)  
            speak(f"Sir, the time is {strTime}")

        elif 'coding' in query or 'code' in query:
            NetBeans = "C:\\Program Files\\NetBeans 8.2\\bin\\netbeans64.exe"
            Thonny = "C:\\Users\\Madhav\\AppData\\Local\\Programs\\Thonny\\thonny.exe"
            PyCharm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"
            VSCode = "C:\\Users\\Madhav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

            speak("Which IDE do you wanna use sir?")
            mknc = Command().lower()
            pycharm_list = {"pycharm", "picharm", "pi charm", "py charm"}
            VSCode_list = {"vscode", "vs code", "v s code"}

            if "netbeans" in mknc:
                print("Starting NetBeans...")
                os.startfile(NetBeans)
            elif mknc == "thonny" or mknc == "thony":
                print("Starting Thonny...")
                os.startfile(Thonny)
            elif mknc in pycharm_list:
                print("Starting Pycharm...")
                os.startfile(PyCharm)
            elif mknc in VSCode_list:
                print("Starting VS Code...")
                os.startfile(VSCode)
                
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = Command()
                to = "madhavampire@gmail.com"    
                sendEmail(to, content)
                print("Sent!!!")
                speak("Email has been sent!")
            except Exception:
                speak("Mail not sent due to some error!")
            
        elif 'name' in query:
            speak('I am Moon')

        else:
            speak("SORRY? How can I help you?")
