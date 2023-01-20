import psycopg2
import time

def moderate_messages():
    # Connect to the database
    connection = psycopg2.connect(
        host="127.0.0.1",
        database="NS-zuildDB",
        user="postgres",
        password="Admin"
    )

    # Create a cursor for database operations
    cursor = connection.cursor()

    # Retrieve all messages from the "messages" table
    cursor.execute("SELECT * FROM New_message")
    messages = cursor.fetchall()

    moderator_name = input("Moderator naam: ")
    moderator_email = input("Moderator email: ")

    # Display the messages
    display_messages(messages, cursor, connection, moderator_name, moderator_email)

def display_messages(messages, cursor, connection, moderator_name, moderator_email):
    # Iterate through each message
    for message in messages:
        print(f"Bericht: {message[1]}\nDatum: {message[2]}\nTijd: {message[3]}\nGebruiker: {message[4]}\nStation: {message[5]}")

        action = input("Wat wil je doen? (Goedkeuren/Verwijderen): ")
        if action.lower() == "goedkeuren":
            approve_message(message[0], moderator_name, moderator_email, cursor, connection)
        elif action.lower() == "verwijderen":
            delete_message(message[0], cursor, connection)
        else:
            print("Ongeldige invoer")

def approve_message(message_id, moderator_name, moderator_email, cursor, connection):
    moderated_date = time.strftime("%d/%m/%y", time.localtime())
    moderated_time = time.strftime("%H:%M:%S", time.localtime())
    cursor.execute(f"UPDATE New_message SET moderated = true, moderator_name = '{moderator_name}', moderator_email = '{moderator_email}', moderated_date = '{moderated_date}', moderated_time = '{moderated_time}' WHERE id = {message_id}")
    connection.commit()
    print("Bericht goedgekeurd")

def delete_message(message_id, cursor, connection):
    cursor.execute(f"DELETE FROM New_message WHERE id = {message_id}")
    connection.commit()
    print("Bericht verwijderd")

moderate_messages()