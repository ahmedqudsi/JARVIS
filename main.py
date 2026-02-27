# main.py
from JARVIS.speech_engine import speak
from JARVIS.speech_listener import listen, start_mute_listener
from JARVIS.commands import execute_command

if __name__ == "__main__":
    start_mute_listener()
    speak("Allow me to introduce myself. I am Jarvis, a virtual artificial intelligence, and I'm here to assist you with a variety of tasks as best I can, 24 hours a day, 7 days a week. Importing all preferences from home interface. Systems are now fully operational.")

    while True:
        wake_word = listen()
        if "jarvis" in wake_word:
            speak("Yes sir?")
            query = listen()
            if query:
                if "exit" in query or "quit" in query:
                    speak("Goodbye sir.")
                    break
                else:
                    execute_command(query)
