import pyttsx3
import tkinter as tk
import threading

def speak_text():
    def speak():
        text = text_entry.get("1.0", tk.END)
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
       
        # Re-enable the button after speech is finished
        speak_button.config(state=tk.NORMAL)

    # Disable the button while speaking
    speak_button.config(state=tk.DISABLED)

    # Create a new thread for speaking
    speak_thread = threading.Thread(target=speak)
    speak_thread.start()

# Create the application window
window = tk.Tk()
window.title("Text-to-Speech Application")
window.geometry("800x300")


# Create the text entry field
text_entry = tk.Text(window, height=13, width=35)
text_entry.pack()

# Create the button to trigger text-to-speech
speak_button = tk.Button(window, text="Speak", command=speak_text)
speak_button.pack()

# Run the application
window.mainloop()



'''

this application is a text to speech application when you type in the text box and click the speak button it will speak the text you typed in the text box   

it uses the pyttsx3 library to convert text to speech and the tkinter library to create the GUI and the threading library to create a new thread for speaking so that the GUI doesn't freeze while speaking

pip install pyttsx3
pip install tkinter
pip install threading


'''
