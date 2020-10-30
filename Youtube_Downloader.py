from tkinter import  *
from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
import csv
from tkinter import ttk
from pytube import YouTube
root = Tk()
root.title('Anji Youtube Downloader')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects1/resources/thanu.ico')
root.geometry('600x400')

link = input("Enter Youtube Link : ")
yt = YouTube(link)

videos = yt.streams.all()
i =1
for stream in videos:
    print(str(i) + "  " + str(stream))
    i +=1
stream_number = int(input("Enter number : "))

video = videos[stream_number-1]
video.download("D:\you tube videos download")

print("downloaded")

root.mainloop()