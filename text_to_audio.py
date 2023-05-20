from gtts import gTTS
import tkinter as tk
import threading

def speak_text():
    def speak():
        text = text_entry.get("1.0", tk.END).strip()
        language = language_var.get()

        if text:
            speech = gTTS(text=text, lang=language)
            speech.save("temp.mp3")
            play_audio("temp.mp3")

        # Re-enable the button after speech is finished
        speak_button.config(state=tk.NORMAL)

    # Disable the button while speaking
    speak_button.config(state=tk.DISABLED)

    # Create a new thread for speaking
    speak_thread = threading.Thread(target=speak)
    speak_thread.start()

def play_audio(file_path):
    import platform
    import subprocess

    if platform.system() == "Darwin":
        subprocess.call(["afplay", file_path])
    elif platform.system() == "Windows":
        subprocess.call(["start", "/WAIT", "powershell", "-Command", f"(New-Object Media.SoundPlayer '{file_path}').PlaySync(); Remove-Item '{file_path}'"])
    else:
        subprocess.call(["aplay", file_path])

# Create the application window
window = tk.Tk()
window.title("Text-to-Speech Application")
window.geometry("800x400")

# Create the text entry field
text_entry = tk.Text(window, height=20, width=40)
text_entry.pack()

# Create the language selection dropdown
language_var = tk.StringVar(window)
language_var.set("en")  # Default language is English

language_label = tk.Label(window, text="Select Language:")
language_label.pack()

language_menu = tk.OptionMenu(window, language_var, "en", "fr", "es", "bn", "hi")  # Add more language options as needed
language_menu.pack()

# Create the button to trigger text-to-speech
speak_button = tk.Button(window, text="Speak", command=speak_text)
speak_button.pack()

# Run the application
window.mainloop()




