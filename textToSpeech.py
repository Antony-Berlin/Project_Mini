import pyttsx

engine = pyttsx.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


text = "hello da bois"
engine.say(text)
engine.runAndWait()