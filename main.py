import tkinter as tk
import customtkinter as ctr
from pytube import YouTube



def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        print("Invalid link")
    print("Download Succesfull")

#System  Settings

ctr.set_appearance_mode("System")
ctr.set_default_color_theme("blue")

# Our app frame

app = ctr.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#Adding UI Elements

title = ctr.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx=10, pady=10)

#Link input

url_var= tk.StringVar()
link = ctr.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Download Button

download = ctr.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run App

app.mainloop()

