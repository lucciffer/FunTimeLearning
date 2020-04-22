import tkinter as tk
from gtts import gTTS
from playsound import playsound

win = tk.Tk()
win.title("Text to speech converter")
win.geometry("400x120")


def textToSpeech():
    text = entry.get()
    speech = gTTS(text=text,lang="en")
    speech.save(r'/home/lucciffer/Luccy/WORK/Projects/Codes/speech.mp3')
    playsound(r'/home/lucciffer/Luccy/WORK/Projects/Codes/speech.mp3')


label = tk.Label(win,text="Enter text: ")
label.grid(row=0,column=0)

entry = tk.Entry(win)
entry.grid(row=1,column=0)

button =  tk.Button(win,text="convert",bg="black",fg="white",font="courier 10",command=textToSpeech)
button.grid(row=1,column=1)

win.mainloop()


#lucciffer
