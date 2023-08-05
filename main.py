import pyttsx3
import speech_recognition
import wikipedia
import webbrowser
import os
import datetime
import time
from googletrans import Translator
from requests import get
import google #import gcloud services enable language.googleapis.com # Google Cloud Natural Language API
import googletrans
import pywhatkit
import wolframalpha

from tkinter import *
# importing YouTube module
from pytube import YouTube
# initializing tkinter
root = Tk()
# setting the geometry of the GUI
root.geometry("400x350")
# setting the title of the GUI
root.title("Youtube video downloader application")

app = wolframalpha.Client("7LQE88-H5EHJ2APH7")

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice changing

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def computational_intelligence(question):
    try:
        client = wolframalpha.Client("7LQE88-H5EHJ2APH7")
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None
      
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        a = "Good morning my Master", "Good morning master", "Hello Omkar Good Morning", "O, Good morning respected sir", "O, good morning Omkar", "Wow! Welcome back Omkar sir"
        speak(random.choice(a))
    elif hour >= 12 and hour < 18:
        b = "Good Afternoon Omkar", "Good Afternoon sir", "Hello Omkar Good Afternoon", "O, Good Afternoon sir", "O, good Afternoon Omkar", "Wow! Welcome back Omkar sir"
        speak(random.choice(b))
    else:

        c = "Good Evening Omkar", "Good Evening sir", "Hello Omkar Good Evening", "O, Good Evening sir", "O, good Evening Omkar", "Wow! Welcome back Omkar sir"
        speak(random.choice(c))

wishMe()
wel = "So, how can i help you sir!", "How can i help", "Give me a command Sir", "Online and ready sir", "What can i do for you", "Please give me a command Sir"
speak(random.choice(wel))
    return query


def CloseAPPS():
    speak("Ok Sir , Wait A second!")

    if 'close youtube' in query:
            os.system("[path/im Chrome.exe")
    elif 'close chrome' in query:
            os.system("path/im Chrome.exe")
    elif 'close telegram' in query:
            os.system("path/im Telegram.exe")
    elif 'close cmd' in query:
            os.system("path/im cmd.exe")  
    elif 'pdf' in query:
            os.system("path/im Acrobat.exe")
    elif 'notepad' in query:
            os.system("path/im notepad.exe")
    speak("Your Command Has Been Succesfully Completed!")

def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("mail id", "mail id")
    server.sendmail("mail id", to, content)
    server.close()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')
    except:
        # print(e)
        print('Say that again please...')
        return 'None'
    return query
  
def Tran():
    speak("Tell me a line")
    line = takeHindi()
    translate = Translator()
    result = translate.translate(line)
    Text = result.text
    speak(f"The translation for this line is:"+Text)

def dicto():
    dicto("Activated Dictionary!")
    dicto("Tell Me The prob!")
    prob = takeCommand()
    if 'meaning' in prob:
        prob = prob.replace("what is the", "")
        prob = prob.replace("jarvis", "")
        prob = prob.replace("of", "")
        prob = prob.replace("meaning of", "")
        result = Diction.meaning(prob)
        speak(f"The Meaning For {prob} is {result}")
    elif 'synonym' in prob:
        prob = prob.replace("what is the", "")
        prob = prob.replace("jarvis", "")
        prob = prob.replace("of", "")
        prob = prob.replace("synonym of", "")
        result = Diction.synonym(prob)
        speak(f"The Synonym For {prob} is {result}")

    elif 'antonym' in prob:
        prob = prob.replace("what is the", "")
        prob = prob.replace("jarvis", "")
        prob = prob.replace("of", "")
        prob = prob.replace("antonym of", "")
        result = Diction.antonym(prob)
        speak(f"The Antonym For {prob} is {result}")
        speak("Exited Dictionary!")

if __name__ == '__main__':
    while True:
        query = takeCommand().lower()
        print(query)

        # logic building for tasks

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        elif"open adobe" in query or "acrobat" in query or "pdf" in query:
            bpath = "D:\\acrobat\\acrobat\\Acrobat\\Acrobat.exe"
            os.startfile(bpath)
        elif"open cmd" in query or "command prompt" in query:
            bpath = "C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(bpath)
        elif"open telegram" in query or "telegram" in query:
            bpath = "D:\\Telegram Desktop\\Telegram.exe"
            os.startfile(bpath)
          
        # ip address
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")














