import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

voices = engine.getProperty('voices')
for voice in voices:
    if voice.name == 'Anna':
        engine.setProperty('voice', voice.id)
        engine.say('''Ні долі, ні волі у мене нема,
        Зосталася тільки надія одна:''')
        engine.runAndWait()
