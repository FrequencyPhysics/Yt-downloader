from pytube import YouTube
from tkinter import *

root = Tk()
root.geometry("500x500")

def yt():
    url = YouTube(str(var1.get()))
    video = url.streams.first()
    video.download()
    lrewijurtgr6u4r32357 = Label(root,text="DOWNLOADED",fg="green",font=("bold"))
    lrewijurtgr6u4r32357.pack(side=BOTTOM)



n1_label = Label(root,text="YOUTUBE DOWNLOADER",font=("arial",25,"bold","underline"))
n1_label.pack(side=TOP)


y1_label = Label(root,text="Paste link here",font=("arial",10,"bold"))
y1_label.place(x=30,y=90)

var1 = StringVar()

e1 = Entry(root,width=50,textvariable=var1)
e1.place(x=150,y=90)

b43735632466235 = Button(root,text="DOWNLOAD",width=20,font=("bold"),command = yt)
b43735632466235.place(x=130,y=150)





root.mainloop()