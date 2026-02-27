# 🧠 JARVIS – AI Desktop Voice Assistant

A fully voice-controlled AI assistant for Windows inspired by Tony Stark’s JARVIS.
This project integrates LLM intelligence, real-time web search, voice cloning, and PC automation.

🚀 Features

🎙️ Voice Activation (Wake word: "Jarvis")

🔊 Realistic AI Voice Response (ElevenLabs TTS)

🌐 Real-Time Information (SerpAPI – Google Search results)

🤖 LLM Intelligence (DeepSeek via OpenRouter)

💻 PC Control (Open apps, search web, execute commands)

🔇 Interrupt System (Say "Mute" anytime to stop speech)

🧵 Background Mute Listener Thread

# 🏗️ Project Structure

JARVIS/
│
├── main.py               # Main execution loop
├── speech_listener.py    # Voice input & mute listener
├── speech_engine.py      # Text-to-speech system
├── ai_service.py         # LLM + Real-time search integration
├── config.py             # API keys & configuration
└── README.md

# ⚙️ Requirements

Python 3.10+

Windows OS

Working Microphone

Internet connection

Install Dependencies

pip install speechrecognition pyaudio requests simpleaudio serpapi

# If pyaudio fails on Windows:

pip install pipwin

pipwin install pyaudio

🔑 API Setup

You will need:

OpenRouter API Key (for DeepSeek model)

SerpAPI Key (for real-time Google results)

ElevenLabs API Key (for JARVIS voice cloning)

Create a config.py file:

OPENROUTER_API_KEY = "your_openrouter_key"

SERP_API_KEY = "your_serpapi_key"

ELEVENLABS_API_KEY = "your_elevenlabs_key"

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

MODEL_NAME = "deepseek/deepseek-chat-v3-0324:free"

Add this to .gitignore:
config.py


# ▶️ Running JARVIS

python main.py

You should hear:

Jarvis online and awaiting your call.

Say:

Jarvis open chrome

Jarvis what's the weather today

Jarvis search artificial intelligence

Interrupt anytime by saying:

Mute

Exit by saying:

Exit

# 🧠 How It Works

1. Voice Input

Uses speech_recognition to capture microphone input.

2. Intent Handling

System commands → Executed locally

Live info queries → Sent to SerpAPI

Conversational queries → Sent to DeepSeek LLM

3. Voice Output

Text is sent to ElevenLabs API → Audio returned → Played via simpleaudio.

4. Mute System

A background thread constantly listens for the word “mute” and stops audio playback instantly.

🛠 Example Commands

Open Notepad

Open Chrome

Open YouTube

Search <query>

Weather today

Latest news

General conversation

# 🔒 Security Notice

Do NOT push API keys to public repositories.

Use environment variables or a local config file.

Rotate keys immediately if exposed.

# 📌 Future Improvements

Add memory system (conversation history)

Add GUI interface

Add local offline mode

Add custom wake word detection

Add system automation (volume control, shutdown, etc.)
