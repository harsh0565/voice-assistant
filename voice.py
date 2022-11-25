import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello Sir, I am your voice assistant. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = .5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
    

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            speak('opening stackoverflow')
            webbrowser.open("https://stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Downloads\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what  the time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
      
        elif 'open vs code' in query:
            codePath = "C:\\Users\\Harsh Sengar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
            
            
        elif 'open whatsapp' in query:
            whatsappPath = "https://web.whatsapp.com"
            os.startfile(whatsappPath)
            
            
        elif 'open gmail' in query:
            emailpath = "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"
            os.startfile(emailpath)
            
        elif 'open our college website' in query:
            webpath = "https://www.abesit.in"
            os.startfile(webpath)
            
            
        elif 'open our presentation' in query:
            wpath = "file:///C:/Users/Harsh%20Sengar/Documents/Voice%20controlled%20Virtual%20Assistant.pdf"
            os.startfile(wpath)
            
        
        elif 'open hackathon website' in query:
            heckathonpath = "https://devfolio.co/hacknovate-4/dashboard"
            os.startfile(heckathonpath)
        elif 'email to harsh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")