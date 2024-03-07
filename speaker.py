import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

engine.say("Hello my lilly friends.")
engine.runAndWait()

# Use microphone or other audio source
with sr.Microphone() as source:
    audio = recognizer.listen(source)
try:
    # Recognize speech using Google Speech Recognition
    text = recognizer.recognize_google(audio)
    engine.say(f"You said: {text}")
    engine.runAndWait()
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
