import tkinter as tk
import customtkinter as ctr
from pytube import YouTube
from PIL import Image, ImageTk
import requests
from io import BytesIO



def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink ,on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
       

        title.configure(text = ytObject.title, text_color="white")
        
        video.download("Downloads")
        finish.configure(text="Succesfully Downloaded")
        invalid.configure(text="")
        
    except:
        invalid.configure(text="Invalid Link")
        finish.configure(text="")
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    per = str(int(percent))
    percentage.configure( text=per + "%")
    percentage.update()
    # Update progressbar
    progressbar.set(float(percent)/100)



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

#Invalid link

invalid = ctr.CTkLabel(app, text="",text_color="red")
invalid.pack()

#Finished Downloading
finish = ctr.CTkLabel(app, text="" ,text_color="green")
finish.pack()


# progress percentage

percentage = ctr.CTkLabel(app, text="0%")
percentage.pack()

progressbar = ctr.CTkProgressBar(app, width=400)
progressbar.set(0.0)
progressbar.pack(padx=10,pady=10)


# Run App

app.mainloop()

