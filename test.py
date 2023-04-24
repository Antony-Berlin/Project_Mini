from img_to_text import*
from textToSpeech import*
engine = ready_speak()
text = extract("example.png")
speak(engine,text)