# 🤖 Jarvis - Voice Assistant

A Python-based voice assistant that listens to voice commands and performs predefined tasks such as opening websites and playing music.

## 📌 About the Project

Jarvis is a beginner-friendly voice assistant built using Python.

The assistant listens for the wake word **"Jarvis"**. Once the wake word is detected, it listens to the user's command, processes it, and performs the corresponding action.

This project helped me understand:

- Speech recognition
- Text-to-speech
- Python functions
- Conditional statements
- Dictionaries
- Modules
- Web browser automation

## ✨ Features

- 🎤 Voice command recognition
- 🔊 Voice responses
- 🌐 Open Google
- ▶️ Open YouTube
- 📸 Open Instagram
- 💬 Open WhatsApp
- 🎵 Play predefined songs
- 🗣️ Wake-word detection using "Jarvis"

## 🛠️ Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- PyAudio
- Webbrowser
- pywin32

## ⚙️ How It Works

```text
User speaks
     ↓
Microphone captures voice
     ↓
SpeechRecognition converts speech to text
     ↓
Jarvis checks for the wake word
     ↓
Jarvis listens for the command
     ↓
Command is processed
     ↓
Required action is performed
     ↓
Jarvis gives a voice response

```


📂 Project Structure

Jarvis-Voice-Assistant/

── Jarvis.py
── musicLibrary.py
── requirements.txt
── README.md



📄 Jarvis.py

Contains the main logic of the voice assistant, including:

- Voice recognition
- Wake-word detection
- Command processing
- Website opening
- Text-to-speech responses


musicLibrary.py

- Contains a Python dictionary that stores song names and their corresponding YouTube links.



🚀 Installation

Install the required libraries:
```
- pip install SpeechRecognition
- pip install pyttsx3
- pip install PyAudio
- pip install pywin32
```

▶️ Run the Project

```python Jarvis.py```

Then say:

```Jarvis```

After Jarvis responds, give a command such as:

```Open Google```



🎯 Example Commands

Voice Command               Action

- Open Google	                Opens Google
- Open YouTube	              Opens YouTube
- Open Instagram	            Opens Instagram
- Open WhatsApp	              Opens WhatsApp
- Play God	                  Plays the predefined song
- Play Mankirat	              Plays the predefined song
- Play Daru                   Plays the predefined song


