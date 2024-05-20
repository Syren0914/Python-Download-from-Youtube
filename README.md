# Python-Download-from-Youtube
 
YouTube Video Downloader
This is a simple YouTube video downloader application built using Python, Tkinter, and CustomTkinter. It allows users to download YouTube videos in the highest available resolution by providing a YouTube link. The application also includes a progress bar and percentage display to show the download progress.

Features
Download YouTube videos in the highest resolution.
Progress bar and percentage display for download status.
User-friendly interface with CustomTkinter.
Error handling for invalid YouTube links.
Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.x installed on your computer.
The following Python libraries installed:
tkinter
customtkinter
pytube
Pillow
requests
You can install the necessary libraries using pip:

bash
Copy code
pip install pytube customtkinter pillow requests
Installation
Clone this repository to your local machine.
bash
Copy code
git clone https://github.com/your-username/youtube-downloader.git
cd youtube-downloader
Ensure all the required libraries are installed as mentioned in the prerequisites.

Run the application.

bash
Copy code
python app.py
Usage
Open the application.
Insert a valid YouTube link into the input field.
Click the "Download" button.
The title of the video will be displayed, and the download progress will be shown.
Once the download is complete, a success message will be displayed.
Code Explanation
Importing Libraries
python
Copy code
import tkinter as tk
import customtkinter as ctr
from pytube import YouTube
from PIL import Image, ImageTk
import requests
from io import BytesIO
Download Function
python
Copy code
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        video.download("Downloads")
        finish.configure(text="Successfully Downloaded")
        invalid.configure(text="")
    except:
        invalid.configure(text="Invalid Link")
        finish.configure(text="")
Progress Callback
python
Copy code
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    per = str(int(percent))
    percentage.configure(text=per + "%")
    percentage.update()
    progressbar.set(float(percent)/100)
GUI Setup
python
Copy code
ctr.set_appearance_mode("System")
ctr.set_default_color_theme("blue")

app = ctr.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

title = ctr.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx=10, pady=10)

url_var = tk.StringVar()
link = ctr.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

download = ctr.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

invalid = ctr.CTkLabel(app, text="", text_color="red")
invalid.pack()

finish = ctr.CTkLabel(app, text="", text_color="green")
finish.pack()

percentage = ctr.CTkLabel(app, text="0%")
percentage.pack()

progressbar = ctr.CTkProgressBar(app, width=400)
progressbar.set(0.0)
progressbar.pack(padx=10, pady=10)

app.mainloop()
Contributing
If you want to contribute to this project, feel free to fork the repository and submit a pull request. Any contributions, such as bug fixes, improvements, or new features, are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
If you have any questions or suggestions, feel free to contact me at [your-email@example.com].