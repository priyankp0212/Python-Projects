import os
from gtts import gTTS
text='Welcome to PriyankMusic!'

#LANGUAGE IN WHICH YOU WANT TO CONVERT
lang='en'

myobj=gTTS(text=text, lang=lang, slow=False)
myobj.save("audio.mp3")
# PLAY THE CONVERTED FILE
os.system("audio.mp3")
