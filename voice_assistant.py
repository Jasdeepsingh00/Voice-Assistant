from urllib.parse import _ResultMixinStr
import pyttsx3   ######------text to speech library 
############## import module pyttsx3 (we have to install this module by using the command pip install pyttsx3 in terminal)
import datetime   # this module is predefined 
import speech_recognition as sr
import wikipedia    # for seraching on wikipedia 
import webbrowser   # open youtube ....
import os        #  for taking access from the system 
import smtplib    #  this is for sending emails
from requests import get   ### for finding the ip address 
import pywhatkit as kit  # pywhatkit is used for sending whatsapp messages 
import pyjokes   # for jokes 
import sys    #  for shut down the system  
import pyautogui   ### used to control the mouse and keyboard to automate interactions with other application 
import time 


from wikipedia import exceptions  #   here we use os module for playing music from my pc

engine=pyttsx3.init('sapi5')   # sapi5 is a microsoft speech api used for inbulit microsoft sound which is situated in or laptop
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)   ### Voice id helps to select differnt voices  voice[0].id (male voice), voice[1].id( female voice)



####-------- audio function  
def speak(audio):  # defining the speak function 
     engine.say(audio)     ### audio speaks engine function 
     engine.runAndWait()



####--------wish me  function 
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon ")
    else:
        speak("Good evening  ")

    speak("I am Voice Assistant sir. please tell me how may i help you ")
    

######----------Take command function 
def takeCommand():
    # it takes microphone input from the user and returns string output
    r=sr.Recognizer()   # recognizer is a class which helps to recognize the audio
    with sr.Microphone() as source:   # using as a sourec microphone
        print("Listening...")
        r.pause_threshold = 1   # this comes from the speech recognitzation model
        audio=r.listen(source,timeout=1,phrase_time_limit=5)   # this comes from the speech recognitzation model 

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')   #  using google for voice recognizion
        print(f"user said:{query}\n")    #  user query will be printed 
    except Exception as e:
        # print(e)

        print("say that again please....")
        return "None"
    return query


#### send email function 
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com","your password")
    server.sendmail("youremail@gmail.com",to,content)
    server.close()



if __name__ == "__main__":       #  defining the main function 
    wishMe()
    while True:    #### while we ue while loop than the loop automatially working 
    # if 1:
        query= takeCommand().lower()

    # logic for executing tasks based on query
        if 'wikipedia'in query :

            speak("Searching Wikipedia..")
            query=query.replace("wikipedia","")   ##  wikipedia replaces by ("") i.e remove wikipedia
            results=wikipedia.summary(query,sentences=2)   # it returs two sentenses from wikipedia 
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir='D:\\New Punjabi Song'
            songs = os.listdir(music_dir)   #  list all files in our computer
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))  #  os.startfiles -- opens the file

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"Sir ,The time is {strTime}")

        elif 'notepad' in query:
            codePath= "C:\WINDOWS\system32"
            os.startfile(codePath)

        elif 'ip address' in query:
            ip=get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif 'open drive D' in query:
            thispc="D:"
            os.startfile(thispc)

        elif 'how are you'in query:
            speak("I am Fine , Thankyou")
            speak("HOw are you")

        elif 'fine' in query or 'good' in query:
            speak("its good to know that you are Fine ")

        elif "Who made you " in query or "who created you" in query:
            speak("I have been created by Mr. Jasdeep singh")

        elif "exit" in query:
            speak("Thanks for giving me your valuable Time ")

        elif "who i am " in query:
            speak("if you talk then definitely your human.")


        elif "joke" in query:
            speak(pyjokes.get_joke())

        elif "I love you " in query:
            speak("It's hard to understand")
######   Shut DOWN     -------------------
        elif "shut down the system " in query:
            os.system("shutdown /s /t 5")
        
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll.SetSuspendState 0,1,0")
    
#############   Switch the window  -------------- for switch the window we use key alt+tab  so in this we give command to keydown alt and press tab ..
        elif "switch the window" in query:
            pyautogui.keyDown("alt")    #### pyauto gui controls the mouse and keyboard to automate interctions
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")


        



########------Send watsappp messages  ---------------
        elif "send message" in query:
             kit.sendwhatmsg("+7668647887","This is testing",11,39)

####### ---- play songs on youtube  ------
        elif "play songs on youtube " in query :
            kit.playonyt("see you again")   

        elif "you can sleep" in query:
            speak("thanks for using me sir , Have a good day ") 
            sys.exit()


######____ closing the application  ----------
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im C:\WINDOWS\system32") 

#### to set an alarm  -------------
        elif "set alarm" in query:
            nn=int(datetime.datetime.now().hour)
            if nn==22:
                music_dir="D:\\New Punjabi Song"
                songs=os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[1]))

          
        elif 'email to jasdeep' in query:
            try:
                speak("what could i say")
                content=takeCommand()  # returns as a string which i speak 
                to="jasdeepEmail@gmail.com"
                sendEmail(to,content)
                speak("Email has been send:")
            except Exception as e:
                print(e)
                speak("sorry my friend jasdeep, i am not able to send this email")
                