import tkinter as tk
from tkinter import ttk
import pytz
from datetime import datetime


def update_time():
    timezone = combobox.get()
    if timezone != "Select a timezone":
        current_time = datetime.now(pytz.timezone(timezone))
        formatted_time = current_time.strftime(
            "%I:%M:%S %p")  # Format time as 12-hour clock
        label.config(text=formatted_time)
    else:
        label.config(text="Please select a timezone")
    label.after(1000, update_time)  # Update time every second


# Create the GUI window
window = tk.Tk()
window.title("Digital Clock, by @foysal-2023")
window.geometry("800x400")

# Create a Combobox with a search capability to select the timezone
timezones = pytz.all_timezones
combobox = ttk.Combobox(window, values=timezones + timezones, state="readonly")
combobox.set("Select a timezone")
combobox.pack(pady=10)

# Create a label to display the time
label = tk.Label(window, font=("Helvetica", 48), fg="black")
label.pack(pady=20)

# Start updating the time
update_time()

# Run the GUI window
window.mainloop()

'''
This is a digital clock application that displays the current time in a selected timezone.
The application uses the pytz module to get a list of all timezones, and then displays them in a Combobox widget.
The user can select a timezone from the Combobox, and the application will display the current time in that timezone.
The application will update the time every second.

if you use linux :
pip3 install pytz
sudo apt install python3-tk

if you use windows:
pip install pytz
pip install tkinter


'''
