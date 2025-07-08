import speech_recognition as sr
import pyttsx3
from assistant.reply_generator import get_ai_reply

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()

def listen():
    """Listen to microphone and return text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        engine = pyttsx3.init()
        engine.say("Sorry, I could not understand.")
        engine.runAndWait()
    except sr.RequestError as e:
        print(f"Request error: {e}")
        return ""

def speak_reply(text):
    """Convert text to speech.
    We will add a Text reply model here in the future."""
    #reply = f"This is jarvis reply to your {text}, Still in development, able to answer accurately soon."
    reply = get_ai_reply(text)
    print(f"Jarvis : {reply}")
    
     # Re-initialize engine each time to prevent audio issues
    engine = pyttsx3.init()
    engine.say(reply)
    engine.runAndWait()

def speak_direct(text):
    """Convert text to speech directly."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
