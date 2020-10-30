from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *


file_size=0

def stratDownload():
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
        ob = YouTube(url)
        #strms = ob.strames.all()
        #for s in strms:
        # print(s)
        strm = ob.streams.first()
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


#starting gui buliding

root = Tk()
root.title('Anji Youtube Downloader')
root.iconbitmap('./resources/thanu.ico')
root.geometry('600x400')


Label1 = Label(root,text="Thanus Youtube Downloader",font=('Helvetica',20),bg="pink",fg="blue")
Label1.pack(side=TOP,pady=30)

urlinput = Entry(root,width=50,font=('Helvetica',15),fg="blue",justify=CENTER)
urlinput.pack(side=TOP,fill=X,padx=10,pady=50)
#downloadbutton

dBtn = Button(root,text="Start Download",font=('Helvetica',15),fg="red",command=stratDownload)
dBtn.pack(side=TOP)


root.mainloop()














