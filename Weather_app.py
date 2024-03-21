# importing tkinter for GUI creation
from tkinter import *

# importing ttk for creating city dropdown options
from tkinter import ttk

# importing requests module to run and get the API information.
import requests

def get_weather():
    city = city_name.get()
    Api = 'd3fc6f5d0d4d212767e28550ff621bcd'
    data = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' +city+ '&appid='+ Api).json()
    weather_result.config(text=data['weather'][0]['description'])
    cur_temp_result.config(text=str(int(data['main']['temp'] - 273.15))) # # converting to celsius
    # In Tkinter, when we use .config() to set the text of a widget, it expects a string value. It ensures that
    # the values are properly displayed in the GUI. Hence converting numeric values to strings.
    min_temp_result.config(text=str(int(data['main']['temp_min']-273.15)))  # converting to celsius
    max_temp_result.config(text=str(int(data['main']['temp_max'] - 273.15)))  # converting to celsius


# calling the main class
root = Tk()

# creating title of the GUI
root.title('Weather App')

# defining the size
root.geometry('400x500')

# setting up the icon on the app
root.iconbitmap('C:\\Users\\Admin\\Desktop\\weather.png')

# setting the background
root.config(background='lightblue')

# creating label for setting title of the app and then placing it at the right position
root_lab= Label(root, bg = 'lightblue', fg = 'blue' , text= "How's the Weather!", font=('Verdana', 20, 'bold'))
root_lab.place(x = 50, y = 20, height= 40, width= 300)

# creating city list
city_list = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

# creating the dropdown for city list, formatting it and placing it
# StringVar is a special type of variable provided by the Tkinter library.
# It's used specifically for storing string values that are associated with Tkinter widgets, such as Entry,
# Label, Button, etc.
city_name = StringVar()
city_dropdown = ttk.Combobox(root, values = city_list,
                          font = ('Verdana', 12, 'bold'), textvariable = city_name)
city_dropdown.place(x = 70, y = 80, height = 40, width = 250)

# Placing button to start the search
Checkbutton= Button(root, text = 'Check', font=('Verdana', 15, 'bold'), command = get_weather)
Checkbutton.place(x = 140, y = 150, height = 50, width = 100)

# creating labels for weather info
weather_label=Label(root, bg = '#0096DC', text = 'Weather', font = ('Verdana', 12, 'bold'))
weather_label.place(x=20, y=220,height= 40, width = 100)

weather_result=Label(root, bg = '#0096DC', text = '', font = ('Verdana', 12, 'bold'))
weather_result.place(x=140, y=220,height= 40, width = 200)

cur_temp=Label(root, bg = '#0096DC', text = 'Temp', font = ('Verdana', 12, 'bold'))
cur_temp.place(x=20, y=280,height= 40, width = 100)

cur_temp_result=Label(root, bg = '#0096DC', text = '', font = ('Verdana', 12, 'bold'))
cur_temp_result.place(x=140, y=280,height= 40, width = 200)

min_temp=Label(root, bg = '#0096DC', text = 'Min', font = ('Verdana', 12, 'bold'))
min_temp.place(x=20, y=340,height= 40, width = 100)

min_temp_result=Label(root, bg = '#0096DC', text = '', font = ('Verdana', 12, 'bold'))
min_temp_result.place(x=140, y=340,height= 40, width = 200)

max_temp=Label(root, bg = '#0096DC', text = 'Max', font = ('Verdana', 12, 'bold'))
max_temp.place(x=20, y=400,height= 40, width = 100)

max_temp_result=Label(root, bg = '#0096DC', text = '', font = ('Verdana', 12, 'bold'))
max_temp_result.place(x=140, y=400,height= 40, width = 200)

# running the mainloop.
root.mainloop()
