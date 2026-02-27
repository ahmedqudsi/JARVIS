# commands.py
import os
import webbrowser
from JARVIS.speech_engine import speak
from JARVIS.ai_service import get_real_time_info, get_ai_response

def execute_command(command):
    speak("YOUR WISH IS MY COMMAND SIR !")
    if "open notepad" in command:
        os.system("notepad")
        speak("Opening Notepad.")
    elif "open chrome" in command:
        os.startfile("chrome.exe")
        speak("Opening Chrome.")
    elif "search" in command:
        term = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={term}")
        speak(f"Searching for {term}.")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif any(word in command for word in ["weather", "news", "score", "price", "today", "time now", "latest"]):
        speak(get_real_time_info(command))
    else:
        speak(get_ai_response(command))
