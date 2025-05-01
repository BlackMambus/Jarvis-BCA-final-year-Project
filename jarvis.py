import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import sys

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def wish_user():
    """Greet the user according to the time."""
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    elif 18 <= hour < 22:
        speak("Good Evening!")
    else:
        speak("Hello!")
    speak("I am Jarvis, your assistant. How can I help you today?")

def take_command():
    """Listen for voice input and return recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that. Please say that again.")
        return ""
    except sr.RequestError:
        speak("Sorry, the speech service is down.")
        return ""
    return query.lower()

def open_website(site):
    """Open a website based on user command."""
    sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://www.github.com",
        "stackoverflow": "https://stackoverflow.com"
    }
    if site in sites:
        speak(f"Opening {site}")
        webbrowser.open(sites[site])
    else:
        speak("Sorry, I don't know that website.")

def tell_time():
    """Tell the current time."""
    str_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {str_time}")

def wikipedia_search(query):
    """Search Wikipedia and read summary."""
    speak("Searching Wikipedia...")
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    except wikipedia.DisambiguationError as e:
        speak("There are multiple results. Please be more specific.")
    except wikipedia.PageError:
        speak("Sorry, I could not find information on that.")
    except Exception as e:
        speak("An error occurred while searching Wikipedia.")

def main():
    wish_user()
    while True:
        query = take_command()
        if query == "":
            continue

        # Exiting the assistant
        if "exit" in query or "quit" in query or "stop" in query:
            speak("Goodbye! Have a nice day.")
            sys.exit()

        # Open websites commands
        elif "open youtube" in query:
            open_website("youtube")
        elif "open google" in query:
            open_website("google")
        elif "open github" in query:
            open_website("github")
        elif "open stackoverflow" in query:
            open_website("stackoverflow")

        # Wikipedia search
        elif "wikipedia" in query:
            search_term = query.replace("wikipedia", "").strip()
            if search_term:
                wikipedia_search(search_term)
            else:
                speak("Please tell me what you want to search on Wikipedia.")

        # Tell time
        elif "time" in query:
            tell_time()

        else:
            speak("Sorry, I don't have the capability to do that yet.")

if __name__ == "__main__":
    main()



    