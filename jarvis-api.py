# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:38:22 2021

@author: Admin
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import cv2

 

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("I am Foram, Please tell me how may I help you")
 

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice
#print(voices[0])#[0]=mail voice,[1]=femail voice
engine.setProperty('voice', voices[1].id)

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
    except Exception as e:
        print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


    
def load_pdf_fold(folder,ext=[".jpg"]):
       images = []
       for filename in os.listdir(folder):
           file_ext = filename.split(".")
       if len(file_ext) ==2 and file_ext[1] in ext:
           print(filename)
           img = cv2.imread(os.path.join(folder,filename))
           if img is not None:
               images.append(img)
       return images

 

def speak(audio):
    engine.say(audio) 

    engine.runAndWait() #Without this command, speech will not be audible to us.

if __name__=="__main__":
    wishme()
    while True:
       query =takeCommand().lower()
       # Logic for executing tasks based on query
       if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
       elif 'open google' in query:
           webbrowser.open("google.com")
       elif 'open youtube' in query:
            webbrowser.open("youtube.com")
       elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
       elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
       
       elif 'open image' in query:
             train=load_pdf_fold("D:\\phoya photo")
             
             image1 = os.listdir(train)
             print(image1)    
             os.startfile(os.path.join(train, image1[0]))
             
       elif 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
      
       elif 'open pdf' in query:
            pdf_Path = "D:\\upload\\BE-MARKSHEET.pdf"
            os.startfile(pdf_Path)
       elif 'open wordfile' in query:
            word_file="D:\\upload\\mtech.docx"
            os.startfile(word_file)


            
       elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com")
       elif 'open github' in query:
            webbrowser.open("https://github.com")
       
       elif 'open camera' in query:
           vid = cv2.VideoCapture(0)
           while(True):
                  ret, frame = vid.read()
                  cv2.imshow('frame', frame)
                  # the 'q' button is set as the
                  # quitting button you may use any
                  # desired button of your choice
                  if (cv2.waitKey(1) & 0xFF == ord('q')):
                      break
  
           # After the loop release the cap object
           vid.release()
           # Destroy all the windows
           cv2.destroyAllWindows()
        
            
            
      
       
             

    

 
    