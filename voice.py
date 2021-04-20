import pyttsx3
import subprocess
import ffmpeg

engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.milena')


def text_to_file(text):
    source_mp3 = "data/voice.mp3"
    out_ogg = "data/voice.ogg"
    engine.save_to_file(text, source_mp3)
    engine.runAndWait()   
    subprocess.run(["ffmpeg", '-i', source_mp3, '-acodec', 'libopus', out_ogg, '-y'])
    return out_ogg
