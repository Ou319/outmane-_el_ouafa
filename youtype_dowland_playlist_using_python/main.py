from tkinter import *
from tkinter import filedialog
from pytube import Playlist
from tkinter import messagebox
from pytube import YouTube

def choose_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        destination_entry.delete(0, 'end')
        destination_entry.insert(0, folder_path)

def download_playlist():
    playlist_url = playlist_url_entry.get()
    destination_path = destination_entry.get()

    try:
        playlist = Playlist(playlist_url)
        for video in playlist.videos:
            video.streams.first().download(output_path=destination_path)
            print(f"Downloaded: {video.title}")
    except Exception as e:
        messagebox.showwarning("","somthing not work")
def download_single_video():
    video_url = playlist_url_entry.get()
    destination_path = destination_entry.get()

    try:
        yt = YouTube(video_url)
    
        
        # Download the video
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=destination_path)
    except Exception as e:
        messagebox.showwarning("","somthing not work")
# Create Tkinter window
window = Tk()
window.title("Download Playlist from YouTube")
window.config(bg="#fff")
window.geometry("500x270+500+100")
window.resizable(False, False)

# Playlist URL entry
playlist_label = Label(window, text="Playlist URL", bg="#fff")
playlist_label.place(x=15, y=37)
playlist_url_entry = Entry(window, bg="#ccc", bd="0")
playlist_url_entry.place(x=15, y=60, width=470, height=38)

# Destination folder entry
destination_label = Label(window, text="Destination Folder", bg="#fff")
destination_label.place(x=15, y=110)
destination_entry = Entry(window, bg="#ccc", bd="0")
destination_entry.place(x=15, y=133, width=390, height=38)

# Browse button
browse_btn = Button(window, text="Browse", bg="blue", fg="#fff", bd="0", activebackground="#0f0", command=choose_folder)
browse_btn.place(x=410, y=133, width=75, height=38)

# Download button
download_btn = Button(window, text="Download", bg="blue", fg="#fff", bd="0", activebackground="#0f0", command=download_playlist)
download_btn.place(x=16, y=200, width=230, height=48)
download_single_btn = Button(window, text="Download Single Video", bg="blue", fg="#fff", bd="0", activebackground="#0f0",command=download_single_video)
download_single_btn.place(x=256, y=200, width=230, height=48)

# Start Tkinter event loop
window.mainloop()
