import tkinter as tk
import psycopg2
import requests

def display_moderated_messages():
    # Maak verbinding met de database
    connection = psycopg2.connect(
        host="127.0.0.1",
        database="NS-zuildDB",
        user="postgres",
        password="Admin"
    )
    cursor = connection.cursor()
    # Haal de moderated berichten op uit de database
    cursor.execute(
        f"SELECT * FROM New_message WHERE moderated = true ORDER BY moderated_date DESC, moderated_time DESC LIMIT 5")
    moderated_messages = cursor.fetchall()
    root.columnconfigure(0, weight=1)
    for i, message in enumerate(moderated_messages):
        # Create a frame for each message and its associated icons
        message_frame = tk.Frame(root, bg='yellow')
        message_frame.grid(row=i+3,column=0,sticky="nsew")

        # Create a label for the message text
        msbericht_label = tk.Label(message_frame, text=f"{message[1]}\n", bg='yellow', font=("Arial", 20))
        msbericht_label.grid(row=i+3,column=0,sticky="wn")
        message_label = tk.Label(message_frame, text=f"Datum: {message[2]}\nTijd: {message[3]}\nGebruiker: {message[4]}\nStation: {message[5]}\n", bg='yellow', font=("Arial", 12))
        message_label.grid(row=i+3,column=0,sticky="ws")
        location = message[5]
        # Haal de faciliteiten van het station op uit de database
        cursor.execute(
            f"SELECT ov_bike, elevator, toilet, park_and_ride FROM station_service WHERE station_city = '{location}'")
        location_facilities = cursor.fetchone()
        if location_facilities[0]:
            # Toon een afbeelding voor OV-fietsen
            ov_bike_img = tk.PhotoImage(file="img_ovfiets.png")
            ov_bike_label = tk.Label(message_frame, image=ov_bike_img, bg='yellow')
            #Dit moet anders neemt python garbage collection de image mee :(
            ov_bike_label.image = ov_bike_img
            ov_bike_label.grid(row=i+3, column=1+1, sticky="e")
        if location_facilities[1]:
            # Toon een afbeelding voor liften
            elevator_img = tk.PhotoImage(file="img_lift.png")
            elevator_label = tk.Label(message_frame, image=elevator_img, bg='yellow')
            elevator_label.image = elevator_img
            elevator_label.grid(row=i+3,column=2+1,sticky="e")
        if location_facilities[2]:
            # Toon een afbeelding voor toiletten
            toilet_img = tk.PhotoImage(file="img_toilet.png")
            toilet_label = tk.Label(message_frame, image=toilet_img, bg='yellow')
            toilet_label.image = toilet_img
            toilet_label.grid(row=i+3, column=3+1, sticky="e")
        if location_facilities[3]:
            # Toon een afbeelding voor P+R
            park_and_ride_img = tk.PhotoImage(file="img_pr.png")
            park_and_ride_label = tk.Label(message_frame, image=park_and_ride_img, bg='yellow')
            park_and_ride_label.image = park_and_ride_img
            park_and_ride_label.grid(row=i+3, column=4+1, sticky="e")

def get_weather(location):
    # Code to make API call and retrieve weather information for the selected location
    api_key = "343670d3dfdfa8265b8024b1498731b3"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()
    # Extract temperature and weather icon from the JSON response
    temperature = round(weather_data["main"]["temp"] - 273.15, 2)
    icon_id = weather_data["weather"][0]["icon"]
    # Display the temperature and weather icon in the GUI
    temperature_label = tk.Label(root, text=f"temperatuur in {location}: {temperature}°C", bg="yellow")
    temperature_label.grid(row=10, column=2, sticky="nsew")
    icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    icon_data = requests.get(icon_url).content
    icon_img = tk.PhotoImage(data=icon_data)
    icon_label = tk.Label(root, image=icon_img, bg="yellow")
    icon_label.image = icon_img
    icon_label.grid(row=9, column=2, sticky="nsew")

root = tk.Tk()
root.configure(bg='yellow')
root.title("Moderated Messages")

location_label = tk.Label(root, text="Select a location:", bg='yellow')
location_label.grid(row=0, column=0, sticky="n")

location = tk.StringVar(value="Utrecht")
location_dropdown = tk.OptionMenu(root, location, "Utrecht", "Amsterdam", "Groningen")
location_dropdown.grid(row=1, column=0, sticky="n")

weather_button = tk.Button(root, text="Check Weather", command=lambda: get_weather(location.get()))
weather_button.grid(row=2, column=0, sticky="n")

display_button = tk.Button(root, text="Display Moderated Messages", command=display_moderated_messages)
display_button.grid(row=3, column=0, sticky="n")

root.after(2000, display_moderated_messages())
# Auto update de weather
root.after(2000, get_weather, location.get())
root.mainloop()