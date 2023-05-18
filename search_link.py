import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar
from googlesearch import search
import webbrowser
import csv

def search_links():
    keyword = keyword_entry.get()
    if not keyword:
        messagebox.showwarning("Empty Keyword", "Please enter a keyword.")
        return

    search_results = search(keyword, num_results=20)  # Adjust the number of results as needed

    links_listbox.delete(0, tk.END)  # Clear previous search results

    links = []
    for result in search_results:
        links.append(result)

    if not links:
        links_listbox.insert(tk.END, "No links found.")
    else:
        for link in links:
            links_listbox.insert(tk.END, link)

def clear_results():
    links_listbox.delete(0, tk.END)

def open_link(event):
    selected_index = links_listbox.curselection()
    if selected_index:
        link = links_listbox.get(selected_index)
        webbrowser.open(link)


def export_links(links):
    filename = "links.csv"

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Links"])

        for link in links:
            writer.writerow([link])

        messagebox.showinfo("Export Successful", f"Links exported to {filename}.")


# Create the main window
window = tk.Tk()
window.title("Link Search, made by @foysal")
window.geometry("800x600")

# Create and pack the keyword label and entry field
keyword_label = tk.Label(window, text="Keyword:")
keyword_label.pack()
keyword_entry = tk.Entry(window)
keyword_entry.pack()

# Create and pack the search button
search_button = tk.Button(window, text="Search", command=search_links)
search_button.pack()

# Create and pack the clear button
clear_button = tk.Button(window, text="Clear Results", command=clear_results)
clear_button.pack()

# Create and pack the scrollbar and listbox for displaying the search results
scrollbar = Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

links_listbox = Listbox(window, yscrollcommand=scrollbar.set)
links_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=links_listbox.yview)

# Bind double click event to open the selected link in the default browser
links_listbox.bind("<Double-Button-1>", open_link)

# Create and pack the export button
export_button = tk.Button(window, text="Export Links", command=lambda: export_links(links_listbox.get(0, tk.END)))
export_button.pack()


# Run the application
window.mainloop()



'''
This is the code for the search link by keyword  and export the links in a csv file and open the link in your default browser
when you run this code you will see a window with a search bar and a search button
you can search any keyword and it will show you the top 20 links
you can click on the link and it will open in your default browser
you can also export the links in a csv file
you can also clear the search result


pip install googlesearch-python
pip install tk



'''