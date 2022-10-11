#   NS Zuil Project main file
#   Rick Schulte
#   11/10/2022

import time

def zuil_bericht(msg, username, station):
    tijd = time.strftime("%H:%M:%S", time.localtime())
    datum = time.strftime("%D", time.localtime())
    f = open("NS-bericht.txt", "a")
    f.write(msg + "\n" + datum + "\n" + tijd + "\n" + username + "\n" + station + "\n")
    f.close()
    print("success")

def testcode():
    devmsg = input("msg")
    devusername = input("username")
    devstation = input("station")
    zuil_bericht(devmsg, devusername, devstation)

testcode()




