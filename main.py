#   NS Zuil Project main file
#   Rick Schulte
#   11/10/2022

import time
import random

#   Module om bericht aan te maken en te plaatsen in NS-bericht.txt
def zuil_bericht(msg, username):
    tijd = time.strftime("%H:%M:%S", time.localtime())
    datum = time.strftime("%d/%m/%y", time.localtime())
    locaties = ["Nieuw Amsterdam", "Emmen", "Utrecht"]
    station = random.choice(locaties)
    if len(msg) > 140:
        print("Bericht mag niet langer zijn dan 140 charachters.")
        exit()
    if username == "":
        username = "anoniem"
    f = open("NS-bericht.txt", "a")
    f.write(msg + "\n" + datum + "\n" + tijd + "\n" + username + "\n" + station + "\n")
    f.close()
    print("success")

def moderatie():
    print("Placeholder")

def testcode():
    devmsg = input("msg")
    devusername = input("username")
#   devstation = input("station")
    zuil_bericht(devmsg, devusername,)

testcode()

#   Sources:
#   Prog3 Final