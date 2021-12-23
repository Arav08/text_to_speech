from gtts import gTTS
import os

myText = input("Write anything and I will say it back to you: ")

language = 'en'
s_language = 'es' #this provides a spanish accent
fr_language = 'fr' #this provides a french accent

output = gTTS(text = myText, lang = language, slow = False)

output.save("output.mp3")

os.system("start output.mp3")