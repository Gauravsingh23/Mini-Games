import tkinter as tk
import random
from tkinter.messagebox import showinfo
x=0
def game():
    global x
    if x==0:
        start.destroy()
        x=x+1
    def check():
        if entry1.get() == str:
            showinfo("Congratulations", "You have guessed the word correctly")
        else:
            showinfo("Sorry", "You need to work hard")
    def resume():
        win.destroy()
        game()
    words = ["lovelyprofessionaluniversity", "unimall", "compterscience", "python", "google", "yahoo", "instagram", "facebook", "oneworld", "youthvibe", "project","verto", "punjab", "race", "balloon", "apple", "banana", "pink", "black", "maingate", "truck", "random","window", "education", "securityoffice"]
    word = random.randint(0, (len(words) - 1))
    str = words[word]
    s = ''.join(random.sample(str, len(str)))
    win = tk.Tk()
    win.title("LPU Jumble Word Game")
    label1 = tk.Label(win, text=s)
    label1.grid(row=0, column=2, padx=8, pady=8)
    entry1 = tk.Entry(win)
    entry1.grid(row=1, column=2,padx=8,pady=8)
    button1 = tk.Button(win, text="Submit", command=check, bg="orange")
    button1.grid(row=3, column=0, padx=8, pady=8)
    button2 = tk.Button(win, text="Try again", command=resume, bg="orange")
    button2.grid(row=3, column=3, padx=8, pady=8)
    win.mainloop()
start=tk.Tk()
start.title("Welcome To Game")
label=tk.Label(start,text="Let's start the game. Click on Play button")
label.grid(row=0,column=0,padx=8,pady=8)
button=tk.Button(start,text="PLAY",command=game,bg="orange")
button.grid(row=2,column=2,padx=8,pady=8)
start.mainloop()