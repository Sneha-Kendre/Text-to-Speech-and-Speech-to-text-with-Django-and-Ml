
from django.shortcuts import render,redirect
import pyttsx3
import speech_recognition as sr
from .models import *
import threading  # Import threading module

# Create your views here.

def base(request):
    return render(request,'base.html')
def index(request):
    return render(request,'index.html')

# Function to handle speech in a separate thread
def text_to_speech(value):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)  # Set speaking rate
    engine.say(value)
    engine.runAndWait()

# Main view function
def some(request):
    value = request.GET.get('inp', '')
    
    # Run the text_to_speech function in a separate thread
    if value:
        speech_thread = threading.Thread(target=text_to_speech, args=(value,))
        speech_thread.start()
    
    return redirect('text-to-speech')



def speech_to_text(request):
    if request.method == "POST":
        print("fdsfsdf")
        # engine=pyttsx3.init()
        # engine.say("hii")
        r = sr.Recognizer() 
        try:
            print("Listening..")
            with sr.Microphone() as source:
                # r.adjust_for_ambient_noise(source)
                r.pause_threshold = 1
                audio = r.listen(source,timeout=5,phrase_time_limit=5)
        
            query = r.recognize_google(audio, language='en-in')
            print("You have said: " + query)
            print("Audio Recorded Successfully!")

        except Exception as e:
            print("Error: " + str(e))
            query = 'None'
        return redirect('speech_to_text')
    return render(request,'speech_to_text.html')

def record(request): 
    if request.method == "POST":
        print("yes")
        # engine=pyttsx3.init()
        # engine.say("hii")
        r = sr.Recognizer() 
        query = 'None'
        try:
            print("Listening..")
            with sr.Microphone() as source:
                # r.adjust_for_ambient_noise(source)
                r.pause_threshold = 1
                audio = r.listen(source,timeout=1,phrase_time_limit=5)
        
            query = r.recognize_google(audio, language='en-in')
            print("You have said: " + query)
            print("Audio Recorded Successfully!")
            

        except Exception as e:
            print("Error: " + str(e))
            query = 'None'
        return render(request,"ajaxtool.html",{"query":query})
        return redirect('/')

# def speech_to_text(request):
#     print("please say something")   

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source)
#         audio = r.listen(source)

#         try:
#             print("Listening..")
#             query = r.recognize_google(audio, language='en-in')
#             print("You have said: " + query)
#             print("Audio Recorded Successfully!")

#         except Exception as e:
#             print("Error: " + str(e))
#             query = 'None'

#         return query
