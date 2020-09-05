from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk as tk

import download as d
import os.path

root = tk()
root.set_theme('arc')
root.geometry("290x300")

song = StringVar()
artist = StringVar()

def download():
    song_name = entry_song.get()
    artist_name = entry_artist.get()
    
    d.getResults(song_name, artist_name)
    watchID = d.parseResults()
    filename = d.download(watchID, song_name, artist_name)

    while True:
        if os.path.isfile(filename):
            messagebox.showinfo(title = "Done!", message = ("Downloaded "+filename))
            break
        
        else:            
            continue
    
    song.set("")
    artist.set("")

label = ttk.Label(root, text="Welcome To Downloader!")
label.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 10)

label_song = ttk.Label(root, text="Enter The Song Name")
label_artist = ttk.Label(root, text = "Enter The Artist Name:")

label_song.grid(row = 1, column = 0, padx = 7, pady = 10)
label_artist.grid(row = 2, column = 0, padx = 7, pady = 10)

entry_song = ttk.Entry(root, textvariable=song)
entry_artist = ttk.Entry(root, textvariable=artist)

entry_song.grid(row = 1, column = 1, padx = 7, pady = 10)
entry_artist.grid(row = 2, column = 1, padx = 7, pady = 10)

download = ttk.Button(root, text="Download!", command = download)
download.grid(row=3, column=0, columnspan=2, padx=7, pady=10)

root['background'] = "#f5f6f7"
root.resizable(0, 0)
root.mainloop()