import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
# Imports

# Initialization
recognizer=sr.Recognizer()
engine=pyttsx3.init()

# Functions
def speak(text):
  engine.say(text)
  engine.runAndWait()

def processCommand(c):
   if "open google" in c.lower():
      speak("opening google...")
      webbrowser.open("https://google.com")
   elif "open stackoverflow" in c.lower():
      speak("opening stack overflow...")
      webbrowser.open("https://stackoverflow.com")
   elif "open youtube" in c.lower():
      speak("opening youtube...")
      webbrowser.open("https://www.youtube.com")
   elif "open instagram" in c.lower():
      speak("opening instagram...")
      webbrowser.open("https://www.instagram.com")
   elif "open twitter" in c.lower():
      speak("opening twitter...")
      webbrowser.open("https://twitter.com")
   elif "open facebook" in c.lower():
      speak("opening facebook...")
      webbrowser.open("https://www.facebook.com")
   elif "open linkedin" in c.lower():
      speak("opening linkedin...")
      webbrowser.open("https://www.linkedin.com")
   elif "open whatsapp" in c.lower():
      speak("opening whatsapp...")
      webbrowser.open("https://www.web.whatsapp.com")
   elif c.lower().startswith("play"):
      song=c.lower().split(" ")[1]
      link=musicLibrary.music[song]
      webbrowser.open(link)

if __name__=="__main__":
  speak("Initializing luna...")
  while True:
    r=sr.Recognizer()

    # recognise speech
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio=r.listen(source,timeout=1,phrase_time_limit=1)
        word=r.recognize_google(audio)
        print("You said: ",word)
        if(word.lower()=="luna"):
          speak('yesss listening')
          with sr.Microphone() as source:
             print("luna listening")
             audio=r.listen(source)
             command=r.recognize_google(audio)
             processCommand(command)
      
    except Exception as e:
          print("Error {0}".format(e))