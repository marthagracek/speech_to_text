import threading
import time
import os
from tkinter import *
import threading
from datetime import datetime
import systemcheck

import speech_recognition
import pyttsx3
recogniser = speech_recognition.Recognizer()



list_of_punctuations = {'comma': ',', 'fullstop': '.', 'full stop': '.',
                        'new line': '\n', 'newline': '\n', 'colon': ':', "exclamation mark": '!', "semicolon": ';', 'question mark': '?', 'hyphen': '-', 'underscore': '_', 'hash': '#'}

fnt1 = ('Arial',12,'bold')
fnt2 = ('Arial',20,'bold')

#Global Variables
btn1Anim = 0
btn2Anim = 0
btn3Anim = 0
rec = 0


lang = 'en-Us'
#global lang


def speakText(text):
    try:
        engine = pyttsx3.init()
        # engine.setProperty()
        #'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
        engine.setProperty('rate', 120)    # Speed percent (can go over 100)
        engine.setProperty('volume', 0.9)  # Volume 0-1
        engine.say("I Heard. "+text)
        engine.runAndWait()
    except Exception as e:
        print("error",e)

def stt():
    global btn1Anim, btn2Anim, btn3Anim, rec, L2, lang

    if(rec ==1):
        L2.delete(0.0,END)
        L2.insert(0.0," "*5+"Calibrating Mic. Please Stay Silent for few Seconds")
        print('Calibrating Microphone')
        print('Please be silent for few seconds.')
        time.sleep(1)
        with speech_recognition.Microphone() as source:
            recogniser.adjust_for_ambient_noise(source,duration=4)
            L2.delete(0.0,END)
            if lang == 'en-Us':
                L2.insert(0.0, " "*25+"             Speak Now in English")
            elif lang == 'hi-In':
                L2.insert(0.0, " "*25+"             Speak Now in Hindi")
            elif lang == 'te-In':
                L2.insert(0.0, " "*25+"             Speak Now in Telugu")
            time.sleep(0.5)



        with speech_recognition.Microphone() as source: 
            print("Say something!")
            try:
                audio = recogniser.listen(source,timeout = 10)
            except Exception as e:
                print("MIC ERROR : ",e)
                

        # recognize speech using Google Speech Recognition
        try:
            detected_text = recogniser.recognize_google(audio, language=lang)
            print('\n\n\n'+ detected_text)
            for x in list_of_punctuations.keys():
                if x in detected_text:
                    detected_text = detected_text.replace(x, list_of_punctuations[x])           
            print('\n\n\n'+ detected_text)
            L2.delete(0.0,END)
            L2.insert(0.0,detected_text)
            speakText(detected_text)
            if lang == 'en-Us':
                temp = str(datetime.now())[:-7]
                temp = temp.replace(" ", "_")
                temp = temp.replace(":", "_")
                temp = "VTT"+temp+".txt"
                file = open(temp,'w')
                file.write(detected_text)
                file.close()
                print("Output Saved in storedText"+temp)

            if "open" in detected_text.lower():
                if "chrome" in detected_text.lower():
                    os.system("start chrome")

                if "paint" in detected_text.lower():
                    os.system("mspaint")

                if "word" in detected_text.lower() and "pad" in detected_text.lower():
                    os.system("start wordpad")
                    
                if "google" in detected_text.lower(): 
                    os.system("start chrome www.google.com")
                    
                if "instagram" in detected_text.lower(): 
                    os.system("start chrome www.instagram.com")
            
        
        except speech_recognition.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            L2.delete(0.0,END)
            L2.insert(0.0," Speech Recognition could not understand audio. Please Speak Clearly Again")
        except speech_recognition.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            L2.delete(0.0,END)
            L2.insert(0.0,"Could not request results from Google Speech Recognition service. Please Check for Internet Connection ")

        time.sleep(2)
        print('\n\n')
        btn1Anim, btn2Anim, btn3Anim, rec = 0,0,0,0
        
        

root = Tk()
root.title("Advance Speech to Text")
root.geometry("500x500+400+10")

N = 3 #change N value to exact number of frames your gif contains for full  play
frames = [PhotoImage(file='micrec.gif',format = 'gif -index  %i' %(i)) for i in range(N)]

def update(ind):
    global btn1Anim, btn2Anim, btn3Anim
    if(btn1Anim==1):
            ind = ind%N
            frame = frames[ind]
            ind += 1
            B1.config(image=frame)
    
    elif btn2Anim == 1:
        ind = ind%N
        frame = frames[ind]
        ind += 1
        B2.config(image=frame)

    elif btn3Anim == 1:
        ind = ind%N
        frame = frames[ind]
        ind += 1
        B3.config(image=frame)    

    root.after(100, update, ind)
        

def multiThreading():
    while True:
        stt()
        

t1 = threading.Thread(target = multiThreading)
t1.start()

def start1():
    global btn1Anim, rec, lang
    if rec == 0:
        btn1Anim = 1
        rec = 1
        lang = 'en-Us'

def start2():
    global btn2Anim, rec, lang
    if rec == 0:
        btn2Anim = 1
        rec = 1
        lang = 'hi-In'

def start3():
    global btn3Anim, rec, lang
    if rec == 0:
        btn3Anim = 1
        rec = 1
        lang = 'te-In'        
        
def stop():
    global btn1Anim, btn2Anim, btn3Anim, rec, lang, L2
    
    btn1Anim, btn2Anim, btn3Anim, rec = 0, 0, 0, 0
    L2.delete(0.0,END)
    

win = Frame(root, bg ='rosy brown')
L1 = Label(win,text="ADVANCE SPEECH TO TEXT")
L1.config(font = fnt2,bg ='powderblue')
L1.place(x=25,y=10,height = 30,width = 450)
L2 = Text(win)
L2.config(font = fnt1)
L2.place(x=25,y=50,height = 200,width = 450)

B1 = Button(win)
photo = PhotoImage(file = "micrec.gif")
B1.config(image=photo,relief = RAISED, command = start1)
B1.config(bg='red')
B1.place(x = 10, y = 260, height = 150, width = 150)

B2 = Button(win)
photo1 = PhotoImage(file = "micrec.gif")
B2.config(image=photo1,relief = RAISED, command = start2)
B2.config(bg='red')
B2.place(x = 175, y = 260, height = 150, width = 150)
B3 = Button(win)
photo2 = PhotoImage(file = "micrec.gif")
B3.config(image=photo2,relief = RAISED, command = start3)
B3.config(bg='red')
B3.place(x = 340, y = 260, height = 150, width = 150)
L3 = Label(win,text="ENGLISH")
L3.config(font = fnt2,bg ='powderblue')
L3.place(x=10,y=430,height = 30,width = 150)
L4 = Label(win,text="HINDI")
L4.config(font = fnt2,bg ='powderblue')
L4.place(x=175,y=430,height = 30,width = 150)
L5 = Label(win,text="TELUGU")
L5.config(font = fnt2,bg ='powderblue')
L5.place(x=340,y=430,height = 30,width = 150)
B4 = Button(win)
B4.config(text = "STOP", relief = RAISED, command = stop)
B4.config(bg='green')
B4.place(x = 220, y = 470, height = 25, width = 70)

win.place(x=0,y=0,height = 500,width = 500)
root.after(0, update, 0)
mainloop()

