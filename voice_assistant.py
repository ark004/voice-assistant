import pyttsx3
import speech_recognition as sr

def listen_and_recognize():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said: " + command)
        return command.lower()
    except sr.UnknownValueError:
        return "Could not understand your audio"
    except sr.RequestError:
        return "Could not request results; check your network connection"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        command = listen_and_recognize()

        if "hello" in command:
            speak("Hello! How can I help you?")

        elif "what is your name" in command:
            speak("I am a simple voice assistant created with Python.")

        elif "what is your next plan" in command:
            speak("nothing!")
            
        elif "exit" in command:
            speak("Goodbye!")    
            break

        else:
            speak("Sorry, I didn't understand your command.")



