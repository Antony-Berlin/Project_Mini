import pyttsx3

def ready_speak():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    return engine

def speak(engine,text):
    engine.say(text)
    engine.runAndWait()