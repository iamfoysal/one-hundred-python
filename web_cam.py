import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class WebcamApp:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        self.root = tk.Tk()
        self.root.title("Webcam Application")

        self.label = tk.Label(self.root)
        self.label.pack()

        self.nav_bar = tk.Frame(self.root)
        self.nav_bar.pack(pady=10)

        self.capture_btn = tk.Button(self.nav_bar, text="Capture Image", command=self.capture_image)
        self.capture_btn.pack(side=tk.LEFT, padx=10)

        self.exit_btn = tk.Button(self.nav_bar, text="Exit", command=self.exit_app)
        self.exit_btn.pack(side=tk.LEFT)

        self.update_frame()

    def capture_image(self):
        ret, frame = self.cap.read()
        flipped_frame = cv2.flip(frame, 1)

        # Open file dialog to choose the save location
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png")])
        
        if file_path:
            cv2.imwrite(file_path, flipped_frame)
            image = Image.fromarray(cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2RGB))
            image.show()
    
    def update_frame(self):
        ret, frame = self.cap.read()
        flipped_frame = cv2.flip(frame, 1)
        image = Image.fromarray(cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2RGB))
        photo = ImageTk.PhotoImage(image)
        self.label.configure(image=photo)
        self.label.image = photo
        self.label.after(10, self.update_frame)

    def exit_app(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = WebcamApp()
    app.run()


