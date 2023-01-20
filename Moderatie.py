import psycopg2
import tkinter as tk

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

    # Create the main window
    window = tk.Tk()
    window.title("Berichten modereren")
    window.geometry("600x400")

    # Create a scrollable frame to hold the messages
    messages_frame = tk.Frame(window)
    messages_frame.pack(fill="both", expand=True)

    messages_canvas = tk.Canvas(messages_frame)
    messages_canvas.pack(side="left", fill="both", expand=True)

    messages_scrollbar = tk.Scrollbar(messages_frame, orient="vertical", command=messages_canvas.yview)
    messages_scrollbar.pack(side="right", fill="y")

    messages_canvas.configure(yscrollcommand=messages_scrollbar.set)

    # Create a frame to hold the messages inside the canvas
    messages_canvas_frame = tk.Frame(messages_canvas)
    messages_canvas_frame.pack()

    messages_canvas.create_window((0, 0), window=messages_canvas_frame, anchor="nw")

    # Retrieve all messages from the "messages" table
    cursor.execute("SELECT * FROM New_message")
    messages = cursor.fetchall()

    # Display the messages
    display_messages(messages, messages_canvas_frame, cursor, connection)

    # Start the main loop
    window.mainloop()

def display_messages(messages, messages_canvas_frame, cursor, connection):
    # Clear any existing message widgets
    for widget in messages_canvas_frame.winfo_children():
        widget.destroy()

    # Iterate through each message
    for message in messages:
        message_frame = tk.Frame(messages_canvas_frame)
        message_frame.pack(fill="x")

        # Display the message text
        message_label = tk.Label(message_frame, text=f"Bericht: {message[1]}\nDatum: {message[2]}\nTijd: {message[3]}\nGebruiker: {message[4]}\nStation: {message[5]}", wraplength=500)
        message_label.pack(side="left")

        # Create "Approve" and "Delete" buttons for each message
        approve_button = tk.Button(message_frame, text="Goedkeuren", command=lambda message_id=message[0]: approve_message(message_id, cursor, connection))
        approve_button.pack(side="right")

        delete_button = tk.Button(message_frame, text="Verwijderen", command=lambda message_id=message[0]: delete_message(message_id, cursor, connection))
        delete_button.pack(side="right")

def approve_message(message_id, cursor, connection, messages_canvas_frame):
    # Mark the message as "approved"
    cursor.execute("UPDATE messages SET approved = true WHERE id = %s", (message_id,))
    connection.commit()
    print("Bericht goedgekeurd:", message_id)
    #Retrieve all messages from the "messages" table after approval
    cursor.execute("SELECT * FROM messages")
    messages = cursor.fetchall()
    # Display the messages after approval
    display_messages(messages, messages_canvas_frame, cursor, connection)

def delete_message(message_id, cursor, connection, messages_canvas_frame):
    # Delete the message
    cursor.execute("DELETE FROM messages WHERE id = %s", (message_id,))
    connection.commit()
    print("Bericht verwijderd:", message_id)
    #Retrieve all messages from the "messages" table after deletion
    cursor.execute("SELECT * FROM messages")
    messages = cursor.fetchall()
    # Display the messages after deletion
    display_messages(messages, messages_canvas_frame, cursor, connection)

moderate_messages()

