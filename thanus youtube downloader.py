from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from PIL import ImageTk,Image
from threading import *

#total file size container
file_size=0
#this gets called for updating percentage...

def progress(stream=None,chunk=None,file_handle=None,remaining=None):
    #gets the percentage of the file that has been downloaded...
    file_downloaded = (file_size-remaining)
    per = (file_downloaded / file_size) * 100
    dBtn.config(text="{:00.0f} % downloaded ".format(per))


def startDownload():
    global file_size
    try:
        url =urlinput.get()
        print(url)
        #changing button text
        dBtn.config(text='Please wait....')
        dBtn.config(state=DISABLED)
        path = askdirectory()
        print(path)
        if path is None:
            return

        #url = "https://www.youtube.com/watch?v=iQxRnBut51g"
        #path = "D:\you tube videos download"
        #create youtube object with url
        ob = YouTube(url,on_progress_callback=progress)
        #strms = ob.strames.all()
        #for s in strms:
        # print(s)
        strm = ob.streams.first()
        file_size=strm.filesize



        #print(strm)
        #print(strm.filesize)
        #print(ob.description)
        #now downloading the video
        strm.download(path)
        print("downloaded")
        dBtn.config(text="Done")
        dBtn.config(state=NORMAL)
        showinfo("Download Finished","Downloaded succesfully")
        urlinput.delete(0, END)

    except Exception as e:
        print(e)
        print("error1....")


def startDownloadThread():
    #create thread
    thread=Thread(target=startDownload)
    thread.start()

#starting gui buliding

root = Tk()
root.title('Anji Youtube Downloader')
root.iconbitmap('./resources/thanu.ico')
root.geometry('800x300')


Label1 = Label(root,text="Thanus Youtube Downloader",font=('Helvetica',20),bg="pink",fg="blue")
Label1.pack(side=TOP,pady=30)
urlinput = Entry(root,width=100,font=('Helvetica',15),fg="blue",justify=CENTER)
urlinput.pack(side=TOP,fill=X,padx=10,pady=50)
#downloadbutton

dBtn = Button(root,width=30,text="Start Download",font=('Helvetica',15),fg="red",command=startDownloadThread)
dBtn.pack(side=TOP)


root.mainloop()














