# Creating a virtual assitant similar to Siri and Alexa using Python
# code copied from https://www.youtube.com/watch?v=AGatX_8gaeM

# PyAudio is a requirement for using the speech recognition module. The instructions are presented on
# the PyPi page for SpeechRecognition. I've also added the installation path in the requirements txt.

import speech_recognition as sr, os, datetime, warnings, random, calendar,wikipedia
import pyttsx3
from gtts import gTTS

def RecordAudio():
    """
    Function used to record audio from the PC mic. Returns text data.
    """
    # Record the audio  
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Hello")
        audio = r.listen(source)

    # Use Google's speech recognition
    data = r.recognize_google(audio)
    print(f"You said: {data}")

    return data


# Get an assistant's response
#todo potential to use the power of Google to have a conversation with someone
# def AssistantResponse(text):

#     print(text)

#     # Convert the text to speech
#     response = gTTS(text =text,lang = "en", slow = False)

#     # Save the converted audio to a file
#     response.save("response.mp3")

#     # Play the audio file
#     #os.system('start response.mp3')

text = RecordAudio()
# AssistantResponse(text)



convertor = pyttsx3.init()
convertor.setProperty('rate',150)
convertor.setProperty('volume',0.7)
convertor.say(text)

convertor.runAndWait()


# A function for wake words
def Wakeword(text):
    WAKE_WORDS = ["hey computer"]

    text = text.lower()

    # Check to see if the user's commands contains a wake word
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    return False


