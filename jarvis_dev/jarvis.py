import pyttsx3;
import webbrowser
import pyautogui
import time
import speech_recognition as sr



def listing():
    r = sr.Recognizer()
    text = ""
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
    return text

def speak(text):
    i = pyttsx3.init()
    i.say(text)
    i.runAndWait()
    
while True:
    choice = listing().lower()
    if choice == "hi":
        print("Hello")
        speak("Hello")
        
    elif "bye" in choice:
        print("Bye, See You soon")
        speak("Bye, See You soon")
        break
    
    elif "open google" in choice:
        print("Opening Google")
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    
    elif "search on google" in choice:
        topic = choice[17:]
        print(f"Searching {topic} on Google ")
        speak(f"Searching {topic} on Google ")
        webbrowser.open("https://www.google.com/search?q="+topic)
    
    elif "open youtube" in choice:
        print("Openin Youtube")
        speak("Openin Youtube")
        webbrowser.open("https://www.youtube.com")
    
    elif "search on youtube" in choice:
        topic = choice[18:]
        print(f"Searching {topic} on Youtube ")
        speak(f"Searching {topic} on Youtube ")
        webbrowser.open("https://www.youtube.com/search?q="+topic)
    
    elif "play song" in choice:
        topic = choice[10:]
        print(f"Playing {topic} on Youtube ")
        speak(f"Playing {topic} on Youtube ")
        webbrowser.open("https://www.youtube.com/search?q="+topic)
        print("Playing...")
        time.sleep(3)
        pyautogui.moveTo(450,350)
        pyautogui.click()
        
        
    else:
        print("I don't Understand ")
        speak("I don't Understand ")
        


