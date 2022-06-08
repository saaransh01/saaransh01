import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am jarvis sir how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print("User said:",query)

    except Exception as e:
        print(e)

        print("Say that again please")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()

#Main logic starts here
if "wikipedia" in query:
    speak("Searching wikipedia...")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences = 2)
    speak("According to wikipedia")
    speak(results)
    print(results)

elif "open google" in query:
    webbrowser.open("www.google.com")

elif "open youtube" in query:
    webbrowser.open("www.youtube.com")

elif "open code" in query:
    codePath = "C:\\Users\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"
    os.start[codePath]

elif " jarvis quit" in query:
    quit()
    speak("Thank you for you time")