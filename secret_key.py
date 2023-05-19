import tkinter as tk
from tkinter import messagebox
from django.core.management.utils import get_random_secret_key

# Function to copy the secret key to the clipboard


def copy_secret_key():
    secret_key = secret_key_entry.get()
    window.clipboard_clear()
    window.clipboard_append(secret_key)
    messagebox.showinfo(
        "Copied", "Secret key has been copied to the clipboard.")

# Function to generate the secret key


def generate_secret_key():
    secret_key = get_random_secret_key()
    secret_key_entry.delete(0, tk.END)
    secret_key_entry.insert(tk.END, secret_key)


# Create the main window
window = tk.Tk()
window.title("Django Secret Key Generator")
window.geometry("800x300")


# Create a label
label = tk.Label(window, text="Django Secret Key:")
label.pack(pady=10)

# Create an entry field
secret_key_entry = tk.Entry(window, width=60, justify="center")
secret_key_entry.pack()

# Create a button to generate the secret key
generate_button = tk.Button(window, text="Generate",
                            command=generate_secret_key)
generate_button.pack(pady=10)

# Create a button to copy the secret key
copy_button = tk.Button(window, text="Copy", command=copy_secret_key)
copy_button.pack(pady=10)

# Start the application
window.mainloop()


'''
This application is a Django secret key generator. It uses the Django get_random_secret_key() function to generate a secret key and then displays it in a text entry field. You can then copy the secret key to the clipboard by clicking the Copy button. 

It uses the tkinter library to create the GUI.

pip install tkinter




'''
