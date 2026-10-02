# EDITH v5 Advanced - FULLY FIXED
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pyautogui
import os
import sys
import random
import threading
import time
import psutil
import spacy

nlp = spacy.load("en_core_web_sm")
engine = pyttsx3.init()
engine.setProperty('rate', 150)
recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why was the computer cold? It left its Windows open.",
    "There are only 10 types of people. Those who understand binary and those who do not."
]

def speak(text):
    """Speak text and wait for completion"""
    print("EDITH:", text)
    try:
        engine.say(text)
        engine.runAndWait()
        time.sleep(0.5)  # IMPORTANT: Wait for speech to complete
    except Exception as e:
        print(f"Speech error: {e}")

def listen():
    """Listen for voice commands"""
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            audio = recognizer.listen(source, timeout=10)
        
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()
    
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"API Error: {e}")
        return ""
    except Exception as e:
        print(f"Listen error: {e}")
        return ""

def save_note(note):
    """Save note to file"""
    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} - {note}\n")
    speak("Note saved successfully.")

def set_reminder(minutes, message):
    """Set a reminder"""
    def reminder():
        time.sleep(minutes * 60)
        speak(f"Reminder. {message}")
    threading.Thread(target=reminder, daemon=True).start()

def run_command(command):
    """Process voice commands"""
    doc = nlp(command)
    words = [t.lemma_.lower() for t in doc]

    if "github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://github.com/HemanthVadakattu1342")

    elif "linkedin" in command:
        speak("Opening LinkedIn.")
        webbrowser.open("https://www.linkedin.com/in/hemanth-vadakattu-54139b330/")

    elif "gmail" in command or "mail" in command:
        speak("Opening Gmail.")
        webbrowser.open("https://mail.google.com")

    elif "chrome" in command:
        speak("Opening Chrome.")
        webbrowser.open("https://google.com")

    elif "spotify" in command:
        speak("Opening Spotify.")
        os.system("start spotify")

    elif "discord" in command:
        speak("Opening Discord.")
        os.system("start discord")

    elif "vs code" in command or "code" in command:
        speak("Opening VS Code.")
        os.system("code")

    elif "calculator" in command:
        speak("Opening Calculator.")
        os.system("calc")

    elif "notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad")

    elif "downloads" in command:
        speak("Opening Downloads folder.")
        os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))

    elif "desktop" in command:
        speak("Opening Desktop folder.")
        os.startfile(os.path.join(os.path.expanduser("~"), "Desktop"))

    elif "documents" in command:
        speak("Opening Documents folder.")
        os.startfile(os.path.join(os.path.expanduser("~"), "Documents"))

    elif "pictures" in command:
        speak("Opening Pictures folder.")
        os.startfile(os.path.join(os.path.expanduser("~"), "Pictures"))

    elif "music" in command:
        speak("Opening Music folder.")
        os.startfile(os.path.join(os.path.expanduser("~"), "Music"))

    elif "battery" in command:
        battery = psutil.sensors_battery()
        if battery:
            percentage = battery.percent
            speak(f"Battery is at {percentage} percent.")
        else:
            speak("Could not get battery information.")

    elif "joke" in command:
        speak(random.choice(jokes))

    elif "time" in words:
        current_time = datetime.datetime.now().strftime("The time is %I:%M %p")
        speak(current_time)

    elif "date" in words:
        current_date = datetime.datetime.now().strftime("Today is %d %B %Y")
        speak(current_date)

    elif "screenshot" in command:
        os.makedirs("screenshots", exist_ok=True)
        filename = os.path.join(
            "screenshots",
            datetime.datetime.now().strftime("screenshot_%Y%m%d_%H%M%S.png")
        )
        pyautogui.screenshot().save(filename)
        speak("Screenshot saved.")

    elif "timer" in command:
        for token in doc:
            if token.like_num:
                minutes = token.text
                speak(f"Opening a {minutes} minute timer.")
                webbrowser.open(
                    f"https://www.google.com/search?q={minutes}+minute+timer"
                )
                return

    elif "remind" in command:
        for token in doc:
            if token.like_num:
                minutes = int(token.text)
                msg = command.split("to", 1)[1] if "to" in command else "Reminder"
                speak(f"I will remind you in {minutes} minutes.")
                set_reminder(minutes, msg)
                return
        speak("Please specify the number of minutes for the reminder.")

    elif "note" in command or "save" in command:
        note = command.replace("save note", "").replace("note", "").replace("save", "").strip()
        if note:
            save_note(note)
        else:
            speak("Please say what you want to save as a note.")

    elif "youtube" in command:
        query = command.replace("youtube", "").replace("open", "").replace("channel", "").strip()
        if query:
            speak(f"Searching YouTube for {query}.")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        else:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

    elif any(x in command for x in ["search", "find", "google", "look up"]):
        query = command.replace("search", "").replace("find", "").replace("google", "").replace("look up", "").strip()
        if query:
            speak(f"Searching Google for {query}.")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            webbrowser.open("https://www.google.com")

    else:
        speak("Sorry, I don't understand that command. Please try again.")

# =====================
# MAIN PROGRAM
# =====================
print("=" * 50)
print("EDITH v5 Advanced - Starting up...")
print("=" * 50)

speak("Hello Boss. How can I help you today?")

while True:
    command = listen()
    
    # Skip if no command detected
    if not command:
        continue
    
    # Check for exit commands
    if any(x in command for x in ["exit", "quit", "goodbye", "close edith", "shut down"]):
        speak("Goodbye Boss.")
        sys.exit()
    
    # Process the command
    run_command(command)
    
    # Small pause before next listen
    time.sleep(1)