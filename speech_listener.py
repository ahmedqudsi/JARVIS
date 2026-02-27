# speech_listener.py
import speech_recognition as sr
import threading
from JARVIS.speech_engine import stop

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio, language='en-in').lower()
    except:
        return ""

def listen_for_mute():
    r = sr.Recognizer()
    mic = sr.Microphone()
    while True:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            try:
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
                if "mute" in r.recognize_google(audio, language='en-in').lower():
                    print("🔇 Mute detected!")
                    stop()
            except:
                pass

def start_mute_listener():
    thread = threading.Thread(target=listen_for_mute, daemon=True)
    thread.start()
