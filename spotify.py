import os
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import io


# Spotify API credentials
client_id = 'c8a776eeddd349bc8a7cd651822ba71d'
client_secret = '91b7e35f07614827883f71c8a220e7d7'

# Authenticate with Spotify API
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Retrieve the latest 50 tracks from Spotify
results = sp.search(q='year:2023', type='track', limit=50)
tracks = results['tracks']['items']

# GUI Setup
window = tk.Tk()
window.title("Spotify Downloader made by @foysal")
window.geometry("800x600")

# Track List
track_list = tk.Listbox(window, width=60)
for i, track in enumerate(tracks, start=1):
    track_name = track['name']
    artist_name = track['artists'][0]['name']
    track_list.insert(i, f"{i}. {track_name} - {artist_name}")
track_list.pack(pady=10)

# Track Selection
selected_track = tk.StringVar()

def download_track():
    selected_index = track_list.curselection()[0]
    selected_track.set(tracks[selected_index]['name'])
    track_name = tracks[selected_index]['name']
    preview_url = tracks[selected_index]['preview_url']
    
    if preview_url is not None:
        response = requests.get(preview_url)
        if response.status_code == 200:
            audio_data = response.content
            
            # Ask the user to choose the download path
            download_path = filedialog.asksaveasfilename(initialdir="/", title="Select Download Path", defaultextension=".mp3", initialfile=f"{track_name}.mp3")
            
            if download_path:
                with open(download_path, "wb") as f:
                    f.write(audio_data)
                print(f"Track '{track_name}' downloaded successfully.")

download_button = tk.Button(window, text="Download", command=download_track)
download_button.pack(pady=10)

# Track Image
track_image_label = tk.Label(window)
track_image_label.pack(pady=10)

# Track Title
track_title_label = tk.Label(window, textvariable=selected_track, height=50, width=100)
track_title_label.pack()

def update_track_info(event):
    selected_index = track_list.curselection()[0]
    selected_track.set(tracks[selected_index]['name'])
    track_image_url = tracks[selected_index]['album']['images'][0]['url']
    response = requests.get(track_image_url)
    if response.status_code == 200:
        track_image_data = response.content
        track_image = Image.open(io.BytesIO(track_image_data))
        track_image = track_image.resize((300, 300), Image.ANTIALIAS)
        track_image = ImageTk.PhotoImage(track_image)
        track_image_label.config(image=track_image)
        track_image_label.image = track_image
        track_title_label.config(text=selected_track.get())

track_list.bind("<<ListboxSelect>>", update_track_info)

window.mainloop()



''''
This is a simple Spotify Downloader that allows you to download any song from Spotify for free. 
It uses the Spotify API to retrieve the latest 50 tracks from Spotify and allows the user to download their favorite track.
The track is downloaded in MP3 format and saved to the user's computer.

The Spotify API is a web API that provides access to Spotify's music library. 
It allows developers to retrieve information about tracks, artists, albums, playlists, etc. 
It also allows developers to create playlists, add tracks to playlists, etc.

Spotify API Documentation: https://developer.spotify.com/documentation/web-api/
Spotify API Reference: https://developer.spotify.com/documentation/web-api/reference/
Spotify API Console: https://developer.spotify.com/console/

Spotify API Endpoints:
- Search for tracks: https://developer.spotify.com/documentation/web-api/reference/#endpoint-search
- Get a Track: https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-track
- Get an Album: https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-an-album
- Get an Artist: https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-an-artist
- Get Several Tracks: https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-several-tracks
- Get Several Albums: https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-several-albums
- Get Several Artists: https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-several-artists
- Get a Playlist: https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-playlist
- Get a List of Current User's Playlists: https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-a-list-of-current-users-playlists
- Create a Playlist: https://developer.spotify.com/documentation/web-api/reference/#endpoint-create-playlist
- Add Items to a Playlist: https://developer.spotify.com/documentation/web-api/reference/#endpoint-add-tracks-to-playlist

Spotify API Authentication:
- Client Credentials Flow: https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow
- Authorization Code Flow: https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-code-flow
- Implicit Grant Flow: https://developer.spotify.com/documentation/general/guides/authorization-guide/#implicit-grant-flow

Spotify API Libraries:

- Python Library:
pip install spotipy (https://pypi.org/project/spotipy/)
pip install pillow (https://pypi.org/project/Pillow/)
pip install requests (https://pypi.org/project/requests/)
pip install tk (https://pypi.org/project/tk/)



'''