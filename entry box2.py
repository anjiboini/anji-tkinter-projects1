from tkinter import  *
from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
import csv
from tkinter import ttk

root = Tk()
root.title('well come to India thanudatabase')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry('600x400')

def myDelete():
    #mylabel.destroy()
    myButton['state'] = NORMAL
    print(myButton.winfo_exists())

def myclick():
    global mylabel
    hello = e.get()
    mylabel=Label(root,text=hello, font=('Helvetica',15), bg="pink" , fg="blue")
    e.delete(0,END)
    mylabel.grid(row=5,column=0,padx=10,pady=10)
    myButton['state'] = DISABLED

e = Entry(root, width = 20, font=('Helvetica',30))
e.grid(row=1,column=0,padx=10,pady=10)

myButton = Button(root,text="Enter you Name", command =myclick)
myButton.grid(row=2,column=0,padx=10,pady=10)

DeleteButton = Button(root,text="Delete Text", command=myDelete)
DeleteButton.grid(row=3,column=0,padx=10,pady=10)


root.mainloop()