from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_resolution = stream.get_highest_resolution()
        highest_resolution.download(output_path=save_path)
        print("Video downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
        return folder
    


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    url = input("Enter the video URL: ")
    save_path = open_file_dialog()
    
    if not save_path:
        print("Please select a folder to save the video.")

    else:
        print("Downloading video...")
        download_video(url, save_path)

