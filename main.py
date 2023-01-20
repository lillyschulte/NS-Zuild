#   NS Zuil Project main file
#   Rick Schulte
#   11/10/2022
from tkinter import *
import psycopg2
import time
import random


def zuil_bericht(msg, username):
    """
    Module om bericht aan te maken en te plaatsen in een PostgreSQL database
    :param msg: Bericht
    :param username: Gerbuikersnaam
    :return:
    """
    tijd = time.strftime("%H:%M:%S", time.localtime())
    datum = time.strftime("%d/%m/%y", time.localtime())
    locaties = ["Amsterdam", "Groningen", "Utrecht"]
    station = random.choice(locaties)
    if len(msg) > 140:
        print("Bericht mag niet langer zijn dan 140 charachters.")
    if len(username) > 20:
        print("Username mag niet langer zijn dan 20 charachters.")
    if username == "":
        username = "anoniem"
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Admin",
                                      host="127.0.0.1",
                                      database="NS-zuildDB")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO New_message (message, date, time, username, station) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (msg, datum, tijd, username, station)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        print("Record inserted successfully into New_message table")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

root = Tk(className="ns-beeldscherm")
root.configure(bg="yellow")

# Create label and entry widgets for "msg" and "username"
label_msg = Label(master=root, text="Bericht:", background="yellow")
label_msg.pack()

msg_entry = Entry(master=root)
msg_entry.pack()

label_username = Label(master=root, text="Gebruikersnaam:", background="yellow")
label_username.pack()

username_entry = Entry(master=root)
username_entry.pack()

# Create a button to submit the inputs
submit_button = Button(master=root, text="Verstuur", command=lambda: zuil_bericht(msg_entry.get(), username_entry.get()))
submit_button.pack()

canvas = Canvas(root, width=200, height=81, background = "yellow")
canvas.pack()
img = PhotoImage(file= 'nslogo.png')
canvas.create_image(100, 41, image=img)
root.mainloop()



def testcode():
    """"""
#    devmsg = input("msg")
#    devusername = input("username")
#    devstation = input("station")
#    zuil_bericht(devmsg, devusername,)
#    moderatie()

testcode()

#   Sources:
#   Prog3 Final

