import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import time
from datetime import datetime
# import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       
    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

# Function to set a reminder
def set_reminder(reminder_time, reminder_message):
    while True:
        # Get the current time
        current_time = datetime.now().strftime("%H:%M")

        # Check if current time matches the reminder time
        if current_time == reminder_time:
            speak(f"Reminder: {reminder_message}")
            break
        # Wait for 3 seconds before checking the time again to reduce unnecessary load
        time.sleep(3)
        
def main_set_reminder():
            speak("Hello, I can help you set reminders.")
            
            # Ask for the reminder time
            speak("What time would you like to set the reminder for? Please say it in HH:MM format.")
            reminder_time = takeCommand()  # Get the time input from user
            
            if not reminder_time:
                speak("Sorry, I didn't catch that. Please say the time in HH:MM format.")
                return

            # Ask for the reminder message
            speak("What would you like the reminder to say?")
            reminder_message = takeCommand()  # Get the message input from user

            if not reminder_message:
                speak("Sorry, I didn't catch that. Please say the reminder message again.")
                return

            # Set the reminder
            speak(f"Reminder set for {reminder_time}. I will remind you.")
            set_reminder(reminder_time, reminder_message)
       


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        
        if 'set reminder' in query:
            main_set_reminder()
        
            # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            # print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")      
        
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com") 
            
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")    

        elif 'play music' in query:
            music_dir = 'C:\\Users\\dell\\Music\\song'
            songs = os.listdir(music_dir)
            # print(songs)    
            os.startfile(os.path.join(music_dir, songs[random.randrange(0,3)])) 
            # use random module to play a song randomly otherwise indexing is use for specific song

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\dell\\Desktop\\sentiment_analysis_project"
            os.startfile(codePath)

        elif 'email to radha' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "senderEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email") 
                # gmail has high security that does not give access to less secure app to send an email select less secure access on from google accpunt security   
        elif 'stop' in query:
                speak("Stopping the assistant.")
                break  