import PyPDF2
from gtts import gTTS
file=open("20-JCS1599.pdf","rb")
reader=PyPDF2.PdfReader(file)
text=""
for page in reader.pages:
    page_text=page.extract_text()
    if page_text:
        text += page_text + '\n'
speech=gTTS(text, lang="en")      
speech.save("output.mp3")
file.close()
print("PDF to audio conversion completed successfully output.mp3 for the audio file.")       