import tkinter as tk                #Importing the Tkinter package.
from tkinter import *               #Importing everything from Tkinter library.
import random                       #Importing random module to take Random values.

global no                           #Declaring global variables.
global score                        #Declaring global variables.
root = Tk()
root.title("Guess Game")            #The title of the game window
root.geometry('600x400')            #The size of the game window
root.configure(bg="light green")    #The color of the background in the game window.
no = random.randint(1, 100)         #Storing any random number between 1-100 in "no" variable
score = 0                           #Variable to keep track of the player score
choice = IntVar()                   #Value holder for integer variable. The value stored by the user is stored in this.


def comp():                         #Is a function which is used to compare the player's input and the computers number
    global score                    #It also increments the score variable after every attempt by the player
    if no < choice.get():
        Label1 = Label(root, text=" Guess a lower Number ",     #Label used to give the player a hint.
                       relief=RIDGE, font=('Roboto', 15))
        Label1.place(relx=0.5, rely=0.6, anchor=CENTER)
        score += 1

    elif no > choice.get():
        Label2 = Label(root, text=" Guess a Higher Number",     #Label used to give the player a hint.
                       relief=RIDGE, font=('Roboto', 15), )
        Label2.place(relx=0.5, rely=0.6, anchor=CENTER)
        score += 1
    else:
        Label3 = Label(root, text="Damn🔥🔥.Right Answer!!",     #Label used to print if the player got the right answer.
                       relief=RIDGE, font=('Roboto', 15))
        Label3.place(relx=0.5, rely=0.6, anchor=CENTER)
        Label5 = Label(root, text=score,
                       relief=RIDGE, font=('Roboto', 15))       #Label used to print the final score of the player.
        Label5.place(relx=0.57, rely=0.5, anchor=CENTER)


def resart():                       #Function used to restart the game/start a new game with new score.
    global no
    global score
    no = random.randint(1, 100)     #Changing the computer's number by selecting any random number between 1-100.
    score = 0                       #Resetting the score to zero.
    Label6 = Label(root, text=score,#Printing the score back to 0.
                   relief=RIDGE, font=('Roboto', 15))
    Label6.place(relx=0.55, rely=0.5, anchor=CENTER)
    return


Labelhead = Label(root, text="Enter any Number between 1 to 100 ",      #Instruction for the player.
                  relief=RIDGE, font=('Roboto', 20))
Labelhead.place(relx=0.5, rely=0.05, anchor=CENTER)

Label4 = Label(root, text="Score = ",                                   #"Score =" being printed in the window.
               relief=RIDGE, font=('Roboto', 15))
Label4.place(relx=0.5, rely=0.5, anchor=CENTER)

ent1 = Entry(root, textvariable=choice, width=3,                        #Entry box where the user inputs his/her guess.
             font=('Roboto', 50), relief=GROOVE)
ent1.place(relx=0.5, rely=0.275, anchor=CENTER)

myButton1 = Button(root, text="GUESS", padx=35, pady=15, command=comp)  #Button which calls the "comp()" function.
myButton1.place(relx=0.5, rely=0.8, anchor=CENTER)

myButton2 = Button(root, text="Quit", padx=45,                          #Button which terminates the window.
                   pady=15, command=root.destroy)
myButton2.place(relx=0.75, rely=0.8, anchor=CENTER)

myButton3 = Button(root, text="Play Again", padx=35,                    #Button which calls the "restart()" function.
                   pady=15, command=resart)
myButton3.place(relx=0.25, rely=0.8, anchor=CENTER)

root.mainloop()                                                         #Calling the mainloop of Tk

#Coded by Aman Rehan, 12001782