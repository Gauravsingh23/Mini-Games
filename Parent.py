
from tkinter import *
from subprocess import call

root=Tk()
root.title("Mini-Games")
root.geometry("1280x720")
#<<================IMAGE================>>
bg_icon=PhotoImage(file="bg.png")
bg_lb1=Label(root,image=bg_icon).pack()

title=Label(root,text="MINI GAMES",font=("roboto",40,"bold"),bg="brown",fg="white",bd=10,relief=GROOVE)
title.place(x=0,y=0,relwidth=1)

button_Frame=Frame(root,bg='orange' )
button_Frame.place(x=100,y=100)

#<<=============functions================>>
def open1():
    call(["python", "jumblewordgame.py"])

def open2():
    call(["python", "Guess.py"])

def open3():
    call(["python", "game.py"])

#<<================BUTTONS================>>

button1=Button(button_Frame,text="Jumble Word",width=20,font=("roboto",14,"bold"),
               bg="Sky blue",fg="white",command = open1).grid(row=3,column=0,pady=10,)

button2=Button(button_Frame,text="Number Guess",width=20,font=("roboto",14,"bold"),
               bg="light green",fg="white",command = open2).grid(row=3,column=1,pady=10)

button3=Button(button_Frame,text="Rock Paper Scissors",width=20,font=("roboto",14,"bold"),
               bg="Sky blue",fg="white",command = open3).grid(row=3,column=2,pady=10)

root.mainloop()