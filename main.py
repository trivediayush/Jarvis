import speech_recognition as sr
import webbrowser
import pyttsx3
import os
from openai import OpenAI
import musicLibrary
from gtts import gTTs
import pygame


recognizer = sr.Recognizer()
engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

def speak(text):
    tts = gTTs(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove('temp.mp3')


def aiProcess(command):
    client = OpenAI(api_key="")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system", "content":"You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
)

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open geegforgeeks" in c.lower():
        webbrowser.open("https://www.geeksforgeeks.org")
    elif "open leetcode" in c.lower():
        webbrowser.open("https://leetcode.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    else:
        # open ai handle the request
        output = aiProcess(c)
        speak(output)



if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        

        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yes, Sir")
                # Listen Command 
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
        
