import tkinter as tk
from googletrans import Translator

win = tk.Tk()
win.title("Language Translator")
win.geometry("400x120")

def translator_func():
    word =  entry.get()
    translator = Translator(service_urls=["translate.google.com"])
    translation = translator.translate(word,dest="fr")
    label1 = tk.Label(win,text=f"Translated text: {translation.text}",bg="black",fg="white")
    label1.grid(row=2,column=0)

label = tk.Label(win,text="Write here: ")
label.grid(row=0,column=0)

entry = tk.Entry(win)
entry.grid(row=1,column=0)

button = tk.Button(win,text="convert",bg="black",fg="white",font="courier 10",command=translator_func)
button.grid(row=1,column=1)

win.mainloop()
