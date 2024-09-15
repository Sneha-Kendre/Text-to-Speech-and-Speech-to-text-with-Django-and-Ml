import pyttsx3
import speech_recognition as sr


engine=pyttsx3.init()
engine.say("please say something")
engine.runAndWait()

def speech_to_text():
    print("please say something")   

    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            print("Listening..")
            query = r.recognize_google(audio, language='en-in')
            print("You have said: " + query)
            print("Audio Recorded Successfully!")

        except Exception as e:
            print("Error: " + str(e))
            query = 'None'

        return query

if __name__ == '__main__':
    speech_to_text()
