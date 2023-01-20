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

    for message in moderated_messages:
        # Maak een label aan voor elk bericht
        message_label = tk.Label(root, text=f"Bericht: {message[1]}\nDatum: {message[2]}\nTijd: {message[3]}\nGebruiker: {message[4]}\nStation: {message[5]}\nModerator: {message[6]}\nModerator email: {message[7]}\nModerated_date: {message[8]}\nModerated_time: {message[9]}", bg='yellow')
        message_label.pack()
        location = message[5]
        # Haal de faciliteiten van het station op uit de database
        cursor.execute(
            f"SELECT ov_bike, elevator, toilet, park_and_ride FROM station_service WHERE station_city = '{location}'")
        location_facilities = cursor.fetchone()
        if location_facilities[0]:
            # Toon een afbeelding voor OV-fietsen
            ov_bike_img = tk.PhotoImage(file="img_ovfiets.png")
            ov_bike_label = tk.Label(root, image=ov_bike_img, bg='yellow')
            ov_bike_label.image = ov_bike_img
            ov_bike_label.pack()
        if location_facilities[1]:
            # Toon een afbeelding voor liften
            elevator_img = tk.PhotoImage(file="img_lift.png")
            elevator_label = tk.Label(root, image=elevator_img, bg='yellow')
            elevator_label.image = elevator_img
            elevator_label.pack()
        if location_facilities[2]:
            # Toon een afbeelding voor toiletten
            toilet_img = tk.PhotoImage(file="img_toilet.png")
            toilet_label = tk.Label(root, image=toilet_img, bg='yellow')
            toilet_label.image = toilet_img
            toilet_label.pack()
        if location_facilities[3]:
            # Toon een afbeelding voor P+R
            park_and_ride_img = tk.PhotoImage(file="img_pr.png")
            park_and_ride_label = tk.Label(root, image=park_and_ride_img, bg='yellow')
            park_and_ride_label.image = park_and_ride_img
            park_and_ride_label.pack()

def get_weather(location):
    # Code to make API call and retrieve weather information for the selected location
    api_key = "343670d3dfdfa8265b8024b1498731b3"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()
    # Extract temperature and weather icon from the JSON response
    temperature = weather_data["main"]["temp"]
    icon_id = weather_data["weather"][0]["icon"]
    # Display the temperature and weather icon in the GUI
    temperature_label = tk.Label(root, text=f"Temperature: {temperature}")
    temperature_label.pack()
    icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    icon_data = requests.get(icon_url).content
    icon_img = tk.PhotoImage(data=icon_data)
    icon_label = tk.Label(root, image=icon_img)
    icon_label.image = icon_img
    icon_label.pack()

root = tk.Tk()
root.configure(bg='yellow')
root.title("Moderated Messages")

location_label = tk.Label(root, text="Select a location:", bg='yellow')
location_label.pack()

location = tk.StringVar(value="Utrecht")
location_dropdown = tk.OptionMenu(root, location, "Utrecht", "Amsterdam", "Groningen")
location_dropdown.pack()

weather_button = tk.Button(root, text="Check Weather", command=lambda: get_weather(location.get()))
weather_button.pack()

display_button = tk.Button(root, text="Display Moderated Messages", command=display_moderated_messages)
display_button.pack()

root.mainloop()
