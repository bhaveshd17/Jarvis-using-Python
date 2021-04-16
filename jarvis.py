import datetime
import os
import smtplib
import random
import sys
import pyjokes
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
from email.message import EmailMessage
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour < 12:
        speak("Hello, Good Morning!")
    elif hour>=12 and hour<4:
        speak("Hello, Good Afternoon!")
    else:
        speak("Hello, Good Evening")
    speak("I am Jarvis, sir. How may i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognising..')
        query = r.recognize_google(audio, language='en-in').lower()
        print(f"User said {query}")
    except Exception as e:
        print("Say that again please..")
        return "None"
    return query


def send_email(receiver_mail, subject, text):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('mail@gmail.com', 'pass')
    email = EmailMessage()
    email['From'] = 'mail@gmail.com'
    email['To'] = receiver_mail
    email['Subject'] = subject
    email.set_content(text)
    server.send_message(email)


email_list = {
    'bhavesh' : 'bhavesh@gmail.com'
}



if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(result)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak("what should i search on google")
            cmd = takeCommand()
            webbrowser.open(cmd)
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_Dir = "E:\\Files\\Songs"
            songs = os.listdir(music_Dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_Dir, rd))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime('%H:%M %p')
            speak(f"sir, Now the time is {strTime}")

        elif "open code" in query:
            path = "C:\\Users\\bhave\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Code.exe"
            os.startfile(path)
        elif "open pycharm" in query:
            path = "D:\\Program Files\\PyCharm Community Edition 2020.3.1\\bin\\pycharm64.exe"
            os.startfile(path)

        elif "send mail" in query:
            speak('To whom you want to send mail ?')
            name = takeCommand()
            receiver_mail = email_list[name]
            speak('What is the subject')
            subject = takeCommand()
            speak('Tell me the text to send')
            text = takeCommand()
            speak('Sending email...')
            send_email(receiver_mail, subject, text)
            speak(f"Mail has been send to {name}")

        elif "send whatsapp message" in query:
            speak('Tell me to Whom You want to send Message!')
            name = takeCommand()
            number_list = {
                'bhavesh' : '+919856487952'
            }
            speak('Tell me Message')
            message = takeCommand()
            now = datetime.datetime.now().strftime("%H:%M:%S")
            hr = int(now.split(':')[0])
            minu = int(now.split(':')[1]) + 2
            pywhatkit.sendwhatmsg(number_list[name], message, hr, minu)



        elif "sleep jarvis" in query:
            speak("Thank You Sir")
            sys.exit()

        elif "close code" in query:
            speak("Closing Visual code")
            os.system("taskkill /f /im Code.exe")

        elif "tell me a jokes" in query:
            randNo = random.randint(0, 20)
            joke = pyjokes.get_jokes(language="en", category="neutral")[randNo]
            speak(joke)