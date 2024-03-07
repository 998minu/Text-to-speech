import asyncio
import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import httpx

async def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        # Speak English
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 0.8)
        engine.say(text)
        engine.runAndWait()
        async with httpx.AsyncClient() as session:
            translator = Translator()
            translated_text =translator.translate(text, dest="hi").text
            print("Hindi translation:", translated_text)

            # Speak Hindi
            engine.setProperty('voice', 'hi-IN')
            engine.say(translated_text)
            engine.runAndWait()


    except sr.UnknownValueError:
        print("Sorry, I could not understand.")

if __name__ == "__main__":
    asyncio.run(main())
