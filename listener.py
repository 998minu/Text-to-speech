import speech_recognition as sr
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
    
try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand.")
    
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Speed of speech (words per minute)
engine.setProperty("volume", 0.8)  # Volume level (0.0 to 1.0)
engine.say(audio)
engine.runAndWait()
