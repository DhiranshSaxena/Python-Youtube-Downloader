from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("400x350")
root.title("Youtube Video Downloader Application")

def download():
    try:
        myVar.set("Downloading..")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video Downloaded Successfully")
    except Exception as e:
        myVar.set("Mistake")
        root.update()
        link.set("Enter Correct Link")

Label(root, text = "Welcome to Youtube \nDownloader Application", font = "Consolas 15 bold").pack()
myVar = StringVar()
myVar.set("Enter the link Below")
Entry(root, textvariable = myVar, width = 40).pack(pady = 10)
link = StringVar()
Entry(root, textvariable = link, width = 40).pack(pady = 10)
Button(root, text = "Download Video", command = download).pack()
root.mainloop