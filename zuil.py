import psycopg2

def display_moderated_messages():
    location = input("Select a location (Utrecht[0], Amsterdam[1], Groningen[2]): ")
    connection = psycopg2.connect(
        host="127.0.0.1",
        database="NS-zuildDB",
        user="postgres",
        password="Admin"
    )
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM New_message WHERE moderated = true ORDER BY moderated_date DESC, moderated_time DESC LIMIT 5")
    moderated_messages = cursor.fetchall()

    for message in moderated_messages:
        print(f"Bericht: {message[1]}\nDatum: {message[2]}\nTijd: {message[3]}\nGebruiker: {message[4]}\nStation: {message[5]}\nModerator: {message[6]}\nModerator email: {message[7]}\nModerated_date: {message[8]}\nModerated_time: {message[9]}")

display_moderated_messages()
