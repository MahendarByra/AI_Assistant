from assistant.wakeword_detector import listen_for_wakeword
from assistant.voice_engine import listen, speak_reply, speak_direct

def main():
    first_run = True
    while True:
        if first_run:
            listen_for_wakeword()  # Wait until "Hi Jarvis" is heard
            print("Jarvis : Hello, I am ready for your command.")
            speak_direct("Hello, I am ready for your command.")
            first_run = False
        command = listen()
        if command:
            if "exit" in command.lower():
                print("Jarvis : Goodbye!... See you soon.")
                speak_direct("Goodbye!... See you soon.")
                break
            else:
                speak_reply(command)

if __name__ == "__main__":
    main()
