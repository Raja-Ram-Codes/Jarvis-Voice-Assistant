import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary


recognizer = sr.Recognizer()


def speak(text):
    print("Speaking:", text)

    voice_engine = pyttsx3.init()
    voice_engine.setProperty("volume", 1.0)
    voice_engine.setProperty("rate", 150)

    voice_engine.say(text)
    voice_engine.runAndWait()
    voice_engine.stop()

def processCommand(c):
     if "open google" in c.lower():
          webbrowser.open("https://google.com")
          speak("opening google")
     elif "open youtube" in c.lower():
          webbrowser.open("https://youtube.com")
          speak("opening youtube")
     elif "open instagram" in c.lower():
          webbrowser.open("https://instagram.com")
          speak("opening instagram")
     elif "open whatsapp" in c.lower():
          webbrowser.open("https://whatsapp.com")
          speak("opening whatsapp")

     elif c.lower().startswith("play"):
            song = c.lower().replace("play ", "").replace(" ", "")
            link = musicLibrary.music[song]
            webbrowser.open(link)
                



if __name__ == "__main__":
    speak("Initializing Jarvis.....")

while True:

# Listen for the word wake "JARVIS"
# Obtain audio from the microphone

    r = sr.Recognizer()
    
    print("recognizing...")
    try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
    
            word = r.recognize_google(audio)
    
            if "jarvis" in word.lower():
                speak("Ya")
    
    # Listen for command
    
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("Command:"  , command)
                    processCommand(command)
    
    
    except Exception as e:  
            print("Error; {0}".format(e))                