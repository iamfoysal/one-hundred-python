import sys
import csv
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from googlesearch import search
from tkinter import Tk, filedialog
import urllib.request


class EmailFinderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Email Finder by @foysal-2023")
        self.setMinimumWidth(400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.keyword_label = QLabel("Keyword:")
        self.layout.addWidget(self.keyword_label)

        self.keyword_input = QLineEdit()
        self.layout.addWidget(self.keyword_input)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_emails)
        self.layout.addWidget(self.search_button)

        self.export_button = QPushButton("Export CSV")
        self.export_button.clicked.connect(self.export_csv)
        self.layout.addWidget(self.export_button)

        self.emails = set()

    def search_emails(self):
        keyword = self.keyword_input.text()
        if not keyword:
            QMessageBox.warning(self, "Warning", "Please enter a keyword.")
            return

        self.emails.clear()

        try:
            for url in search(keyword, num_results=10):  # You can adjust the number of search results here
                self.find_emails_from_url(url)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

        QMessageBox.information(self, "Info", "Email search completed.")

    def find_emails_from_url(self, url):
        try:
            response = urllib.request.urlopen(url)
            html = response.read().decode('utf-8')
            emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', html)
            for email in emails:
                self.emails.add(email)
        except Exception as e:
            print(f"Error fetching emails from {url}: {str(e)}")

    def export_csv(self):
        if not self.emails:
            QMessageBox.warning(self, "Warning", "No emails to export.")
            return

        try:
            root = Tk()
            root.withdraw()
            save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
            if save_path:
                with open(save_path, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Email"])
                    for email in self.emails:
                        writer.writerow([email])
                QMessageBox.information(self, "Info", "CSV export completed.")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmailFinderWindow()
    window.show()
    sys.exit(app.exec())


'''
This is a simple email finder app that uses Google search to find email addresses from the web.
It uses the googlesearch Python library to perform the search and the regular expression module to extract email addresses from the HTML content of the web pages.
The app has a simple GUI built using the PyQt5 library.
The app can be used to find email addresses from the web for a given keyword.
The app can also export the email addresses to a CSV file.

sudo apt install python3-pyqt5 
'''