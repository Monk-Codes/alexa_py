import speech_recognition as sr
import webbrowser
import pyttsx3
# Imports

# Initialization
recognizer=sr.Recognizer()
engine=pyttsx3.init()

# Functions
def speak(text):
  engine.say(text)
  engine.runAndWait()

def processCommand(c):
   print(c)
   pass

if __name__=="__main__":
  speak("Initializing Alexa...")
  while True:
    r=sr.Recognizer()

    # recognise speech
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio=r.listen(source,timeout=2,phrase_time_limit=1)
        word=r.recognize_google(audio)
        print("You said: ",word)
        if(word.lower()=="alexa"):
          speak('yesss listening')
          with sr.Microphone() as source:
             print("alexa listening")
             audio=r.listen(source)
             command=r.recognize_google(audio)
             processCommand(command)
      
    except Exception as e:
          print("Error {0}".format(e))