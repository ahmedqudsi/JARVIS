# speech_engine.py
import requests
import simpleaudio as sa
from JARVIS.conapi import ELEVENLABS_API_KEY, VOICE_ID

stop_speaking = False

def speak(text):
    global stop_speaking
    stop_speaking = False
    print(f"JARVIS: {text}")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": "sk_6cd5a000c214fd1cfcb28dbbae782781179f60398973c0b2"
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.9
        }
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            audio_file = "jarvis_voice.wav"
            with open(audio_file, "wb") as f:
                f.write(response.content)

            wave_obj = sa.WaveObject.from_wave_file(audio_file)
            play_obj = wave_obj.play()
            while play_obj.is_playing():
                if stop_speaking:
                    play_obj.stop()
                    break
        else:
            print("Error generating JARVIS voice:", response.text)
    except Exception as e:
        print("Speech error:", e)

def stop():
    global stop_speaking
    stop_speaking = True
