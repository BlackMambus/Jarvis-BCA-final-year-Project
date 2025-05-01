import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pywhatkit
import os

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except Exception as e:
        print("Could not understand. Try again.")
        speak("Sorry, I did not catch that.")
        return "none"

def greet_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I help you today?")

def run_jarvis():
    greet_user()
    while True:
        command = listen_command()

        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time}")

        elif 'date' in command:
            date = datetime.datetime.now().strftime('%B %d, %Y')
            speak(f"Today is {date}")

        elif 'open youtube' in command:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")

        elif 'open google' in command:
            webbrowser.open("https://google.com")
            speak("Opening Google")

        elif 'play' in command:
            song = command.replace('play', '')
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 2)
            speak(info)

        elif 'open notepad' in command:
            os.system("notepad.exe")

        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break

        else:
            speak("I am not sure how to do that yet.")

if __name__ == "__main__":
    run_jarvis()


