# MIRA AI Assistant

A voice-controlled desktop assistant built with Python and Tkinter. MIRA listens to English voice commands, replies out loud, and can open common websites, apps and folders.

## Features

- Voice commands using speech recognition
- Spoken replies using text-to-speech
- Opens YouTube, Google, Notepad, Calculator, Downloads, Documents and your user folder
- Tells the current time
- Greets you based on the time of day (morning, afternoon, evening)
- Simple dark-themed Tkinter interface

## Requirements

- Windows (uses `os.startfile` and the Windows "Zira" voice)
- Python 3.9 or newer
- A working microphone
- An internet connection (speech recognition uses Google's web service)

## Setup

```bash
pip install -r requirements.txt
python main.py
```

If `PyAudio` fails to install with pip, try:

```bash
pip install pipwin
pipwin install pyaudio
```

## Example commands

- "Open YouTube"
- "Open Google"
- "Open Notepad"
- "Open Calculator"
- "Open Downloads"
- "What time is it"
- "What is your name"
- "Hello"
- "Goodbye"

## How it works

1. Click **LISTEN TO MIRA** and speak a command.
2. The microphone audio is converted to text with the `SpeechRecognition` library.
3. The command text is matched against known commands in `handle_command()`.
4. MIRA runs the action and speaks the reply using `pyttsx3`.

## Built with

- Python
- Tkinter
- pyttsx3
- SpeechRecognition

## Future improvements

- Cross-platform support (macOS and Linux)
- Close the app on "goodbye"
- More commands (weather, search, reminders)
- Integrate an AI/LLM model for natural conversations
- Sinhala language support
