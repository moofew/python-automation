import tkinter as tk
from tkinter import filedialog
from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_video(url, save_path):
    try:
        yt = YouTube(url, on_progress_callback=on_progress, use_po_token=True)
        print("Video Title: " + yt.title)
        
        ys = yt.streams.get_highest_resolution()
        print("Downloading video...")
        ys.download(output_path=save_path)
        print("Download complete!")

    except Exception as e:
        print("Error: " + str(e))

def open_file_dialog(): 
    folder = filedialog.askdirectory()
    if folder:
        print("Selected Folder: " + folder)
    else:
        print("Invalid Folder. ")

    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    link = input("Please enter a YouTube URL: ")
    dir = open_file_dialog()

    if dir:
        print("Starting Download...")
        download_video(link, dir)
    else:
        print("Invalid Location.")