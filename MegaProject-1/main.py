
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "4f133d1e03c749f5af747d25d5b6fa3e"


def speak_old(text):
    engine.say(text)
    engine.runAndWait()



def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

      # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3") 


# def speak(text, rate=150):  # Default rate is 150 words per minute
#     try:
#         # Initialize the TTS engine
#         engine = pyttsx3.init()

#         # Set the speaking rate
#         engine.setProperty('rate', rate)

#         # Speak the text
#         engine.say(text)
#         engine.runAndWait()

#     except Exception as e:
#         print(f"An error occurred: {e}")



def aiProcess(command):
    client = OpenAI(api_key="<Your Key Here>",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
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
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in command:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?category=business&apiKey={newsapi}")
            if r.status_code == 200:
                # Parse the JSON response
                data = r.json()
                articles = data.get('articles', [])
                
                if articles:
                    speak("Here are the top news headlines:")
                    for article in articles:
                        speak(article['title'])
                else:
                    speak("Sorry, I couldn't find any news at the moment.")
            else:
                speak(f"Error fetching news: {r.status_code}")
        except requests.RequestException as e:
            speak("Sorry, I couldn't connect to the news service.")
            print(f"Error: {e}")
    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)   













if __name__ == "__main__":
    speak("Initializing Jarvis....")
    recognizer = sr.Recognizer()
    # while True:
    #     #Listen for wake word "jarvis"
    #     #obtain audio from the microphone
    #     r = sr.Recognizer()
          
    #     try:
    #       with sr.Microphone() as source:
    #         print("Listening..")
    #         # audio =  r.listen(source , timeout=2 , phrase_time_limit=1)
    #         audio = r.listen(source, timeout=5, phrase_time_limit=10)

        
    #         print("recognizing...")
  
    #         word = r.recognize_google(audio)
    #         if(word.lower() == "jarvis"):
    #             speak("Ya")
    #             # Listen for command
    #             with sr.Microphone() as source:
    #                 print("Jarvis Active...")
    #                 audio = r.listen(source)
    #                 command = r.recognize_google(audio)

    #                 processCommand(command)

    #     except Exception as e:
    #         print("Error; {0}".format(e))

    while True:
        try:
            # Listen for the wake word "jarvis"
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

                print("Recognizing...")
                word = recognizer.recognize_google(audio)

                if word.lower() == "jarvis":
                    speak("Yes, I'm listening...")

                    # Listen for a command
                    with sr.Microphone() as source:
                        print("Jarvis Active... Speak your command.")
                        recognizer.adjust_for_ambient_noise(source)
                        audio_command = recognizer.listen(source, timeout=5)

                        try:
                            command = recognizer.recognize_google(audio_command)
                            print(f"Command recognized: {command}")
                            processCommand(command)

                        except sr.UnknownValueError:
                            speak("Sorry, I didn't catch that. Please try again.")
                        except sr.RequestError as e:
                            speak("There was an issue with the speech recognition service.")
                            print(f"API error: {e}")

        except sr.UnknownValueError:
            print("No speech detected or unrecognized.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}")


