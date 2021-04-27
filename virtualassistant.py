# Creating a virtual assitant similar to Siri and Alexa using Python
# code copied from https://www.youtube.com/watch?v=AGatX_8gaeM

import speech_recognition as sr, os, datetime, warnings, random, calendar,wikipedia
from gtts import gTTS

#ignore warning messages
def RecordAudio():

    #Record the audio
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Hello")
        audio = r.listen(source)

    #Use Google's speech recognition
    data = r.recognize_google(audio)
    print(f"You said: {data}")

    return data

RecordAudio()

# #Get an assistant's response
def AssistantResponse(text):

    print(text)

    #Convert the text to speech
    response = gTTS(text =text,lang = "en", slow = False)

    #Save the converted audio to a file
    response.save("response.mp3")

    #Play the audio file
    os.system('start response.mp3')

text = "Pour some Sugar on me, yeah yeah yeah"
AssistantResponse(text)

#A function for wake words
def Wakeword(text):
    WAKE_WORDS = ["hey computer"]

    text = text.lower()

    #check to see if the user's commands contains a wake word
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    return False


