import speech_recognition as sr
from googletrans import Translator
import pyttsx3
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data
s= recordAudio()
translator = Translator()
detected=translator.detect(s)
d=(translator.translate(s,src=detected.lang,dest='hindi').text)
print(d)
print(translator.translate(d,src='hindi',dest='english').text)

"""

print(translator.translate(d,src=detected.lang,dest='english').text)

input("Enter")"""
