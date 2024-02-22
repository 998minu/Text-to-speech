from gtts import gTTS

text = "This is a simple text to speech conversion!"
language = 'en'
slow = False 

tts = gTTS(text=text, lang=language, slow=slow)
tts.save("output.mp3")

print("Speech saved to output.mp3")