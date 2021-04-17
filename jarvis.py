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
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from jarvisGui import Ui_JarvisGui


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


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
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
    def TaskExecution(self):
        wishMe()
        while True:
            self.query = self.takeCommand().lower()
            if "wikipedia" in self.query:
                self.query = self.query.replace("wikipedia", "")
                result = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                speak(result)

            elif "open youtube" in self.query:
                webbrowser.open("youtube.com")
            elif "open google" in self.query:
                speak("what should i search on google")
                cmd = self.takeCommand()
                webbrowser.open(cmd)
            elif "open stackoverflow" in self.query:
                webbrowser.open("stackoverflow.com")
            elif "play music" in self.query:
                music_Dir = "E:\\Files\\Songs"
                songs = os.listdir(music_Dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_Dir, rd))

            elif "the time" in self.query:
                strTime = datetime.datetime.now().strftime('%H:%M %p')
                speak(f"sir, Now the time is {strTime}")

            elif "open code" in self.query:
                path = "C:\\Users\\bhave\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Code.exe"
                os.startfile(path)
            elif "open pycharm" in self.query:
                path = "D:\\Program Files\\PyCharm Community Edition 2020.3.1\\bin\\pycharm64.exe"
                os.startfile(path)

            elif "send mail" in self.query:
                speak('To whom you want to send mail ?')
                name = self.takeCommand()
                receiver_mail = email_list[name]
                speak('What is the subject')
                subject = self.takeCommand()
                speak('Tell me the text to send')
                text = self.takeCommand()
                speak('Sending email...')
                send_email(receiver_mail, subject, text)
                speak(f"Mail has been send to {name}")

            elif "send whatsapp message" in self.query:
                speak('Tell me to Whom You want to send Message!')
                name = self.takeCommand()
                number_list = {
                    'bhavesh': '+919856487952'
                }
                speak('Tell me Message')
                message = self.takeCommand()
                now = datetime.datetime.now().strftime("%H:%M:%S")
                hr = int(now.split(':')[0])
                minu = int(now.split(':')[1]) + 2
                pywhatkit.sendwhatmsg(number_list[name], message, hr, minu)



            elif "sleep jarvis" in self.query:
                speak("Thank You Sir")
                sys.exit()

            elif "close code" in self.query:
                speak("Closing Visual code")
                os.system("taskkill /f /im Code.exe")

            elif "tell me a jokes" in self.query:
                randNo = random.randint(0, 20)
                joke = pyjokes.get_jokes(language="en", category="neutral")[randNo]
                speak(joke)

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisGui()
        self.ui.setupUi(self)
        self.ui.start.clicked.connect(self.startTask)
        self.ui.stop.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("img/bg1.gif")
        self.ui.bg.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("img/bg.gif")
        self.ui.img.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())


