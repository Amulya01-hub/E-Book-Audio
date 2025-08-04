from gtts import gTTS
file=open('sample.txt','r').read()
language='en'
speaker= gTTS(text=str(file),lang=language,slow=False)
speaker.save('kitty.mp3')