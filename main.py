
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pyttsx3
import speech_recognition as sr
import threading
import webbrowser
import os

# MIRA voice setup
engine = pyttsx3.init()
engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")
zira = next(
    (v for v in voices if "zira" in v.name.lower()),
    None
)

if zira:
    engine.setProperty("voice", zira.id)


def speak(text):
    def run_voice():
        engine.say(text)
        engine.runAndWait()

    threading.Thread(target=run_voice, daemon=True).start()


def greet():
    hour = datetime.now().hour

    if hour < 12:
        greeting = "Good morning!"
    elif hour < 17:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"

    message.config(text=f"{greeting}\nMIRA is online.")
    speak(f"{greeting} Mee-rah is online. How can I help you sir?")


def listen():
    listen_button.config(text="Listening...", state="disabled")
    message.config(text="I'm listening. Please speak in English.")

    threading.Thread(target=recognize_voice, daemon=True).start()


def recognize_voice():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)

        command = recognizer.recognize_google(audio, language="en-US")
        root.after(0, lambda: handle_command(command))

    except sr.WaitTimeoutError:
        root.after(0, lambda: show_result("I didn't hear anything. Try again."))

    except sr.UnknownValueError:
        root.after(0, lambda: show_result("Sorry, I couldn't understand."))

    except sr.RequestError:
        root.after(0, lambda: show_result("Speech service unavailable. Check internet."))

    except Exception as error:
        root.after(0, lambda: show_result("Microphone error. Check your microphone."))


def show_result(text):
    message.config(text=text)
    listen_button.config(text="LISTEN TO MIRA", state="normal")
    speak(text)


def handle_command(command):
    import os
    message.config(text=f"You said: {command}")

    cmd = command.lower()

    if "open youtube" in cmd : 
        import os
        webbrowser.open("https://www.youtube.com")
        reply = "Opening YouTube."

    elif "open google" in cmd:
        webbrowser.open("https://www.google.com")
        reply = "Opening Google."

    elif "open notepad" in cmd:
        os.startfile("notepad.exe")
        reply = "Opening Notepad."

    elif "open calculator" in cmd or "open calc" in cmd:
        os.startfile("calc.exe")
        reply = "Opening Calculator."

    elif "open download" in cmd:
        os.startfile(os.path.expanduser("~/Downloads"))
        reply = "Opening Downloads folder."

    elif "open documents" in cmd:
        os.startfile(os.path.expanduser("~/Documents"))
        reply = "Opening Documents folder."

    elif "open file explorer" in cmd or "open folders" in cmd:
        os.startfile(os.path.expanduser("~"))
        reply = "Opening your user folder."

    elif "what time" in cmd or "current time" in cmd:
        reply = "The time is " + datetime.now().strftime("%I:%M %p")

    elif "hello" in cmd or "hi mira" in cmd:
        reply = "Hello! I'm here to help you."

    elif "your name" in cmd:
        reply = "My name is Mee-rah. Your personal AI assistant."

    elif "stop" in cmd or "goodbye" in cmd:
        reply = "Okay! Talk to you later."

    else:
        reply = "I heard you say " + command + ". I don't know that command yet."

    message.config(text=f"You said: {command}\n\nMIRA: {reply}")
    listen_button.config(text="LISTEN TO MIRA", state="normal")
    speak(reply)


# Main window
root = tk.Tk()
root.title("MIRA AI Assistant")
root.geometry("420x340")
root.configure(bg="#101426")
root.resizable(False, False)

def start_drag(event):
    root.x = event.x
    root.y = event.y

def drag_window(event):
    x = root.winfo_pointerx() - root.x
    y = root.winfo_pointery() - root.y
    root.geometry(f"+{x}+{y}")


title = tk.Label(
    root, text="M I R A",
    font=("Segoe UI", 28, "bold"),
    fg="#66E3FF", bg="#101426"
)
title.bind("<Button-1>", start_drag)
title.bind("<B1-Motion>", drag_window)

title.pack(pady=(20, 10))

message = tk.Label(
    root, text="Your personal assistant",
    font=("Segoe UI", 10),
    fg="white", bg="#101426",
    justify="center", wraplength=380
)
message.pack(pady=15)

start_button = tk.Button(
    root, text="START MIRA",
    font=("Segoe UI", 10, "bold"),
    fg="#101426", bg="#66E3FF",
    relief="flat", padx=20, pady=8,
    command=greet
)
start_button.pack(pady=5)

listen_button = tk.Button(
    root, text="LISTEN TO MIRA",
    font=("Segoe UI", 10, "bold"),
    fg="white", bg="#273653",
    activebackground="#354969",
    relief="flat", padx=20, pady=8,
    command=listen
)
listen_button.pack(pady=5)

root.after(700, greet)
root.mainloop()
