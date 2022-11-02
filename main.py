#   NS Zuil Project main file
#   Rick Schulte
#   11/10/2022

import time
import random
from tkinter import *
def zuil_bericht(msg, username):
    """
    Module om bericht aan te maken en te plaatsen in NS-bericht.txt
    :param msg: Bericht
    :param username: Gerbuikersnaam
    :return: 
    """""
    tijd = time.strftime("%H:%M:%S", time.localtime())
    datum = time.strftime("%d/%m/%y", time.localtime())
    locaties = ["Nieuw Amsterdam", "Emmen", "Utrecht"]
    station = random.choice(locaties)
    if len(msg) > 140:
        print("Bericht mag niet langer zijn dan 140 charachters.")
        exit()
    if len(username) > 20:
        print("Username mag niet langer zijn dan 20 charachters.")
        exit()
    if ";" in msg or username:
        print("fout")
        exit()
    if username == "":
        username = "anoniem"
    f = open("NS-bericht.txt", "a")
    f.write(msg + ";" + datum + ";" + tijd + ";" + username + ";" + station + "\n")
    f.close()
    print("success")

def moderatie():
    f = open("NS-bericht.txt", "r")
    lines = f.readlines()
    #schermlijst[]



root = Tk()

#img = ImageTK.PhotoImage(file = 'scsweb.png')

def onclick():
    base = int(entry.get())
    square = base ** 2
    outcome = f'square of: {base} = {square}'
    label['text'] = outcome

label = Label(master = root,
              text = 'test',
              background = 'yellow',
              foreground= 'purple',
              font=('Ariel', 16, 'bold italic'),
              width = 15,
              height = 8,)
label.pack()

button = Button(master=root,text='press', command = onclick)

button.pack(pady=50)

entry = Entry(master=root)
entry.pack(pady=10, padx=10)

root.mainloop()


def testcode():
    """"""
    devmsg = input("msg")
    devusername = input("username")
#   devstation = input("station")
    zuil_bericht(devmsg, devusername,)

testcode()

#   Sources:
#   Prog3 Final

