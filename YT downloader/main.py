
from tkinter import *
from pytube import YouTube

win = Tk()
win.geometry('500x300')
win.title('YT video downloader')

label_1 = Label(win, text='YT video downloader', font='arial 20 bold').pack()
link = StringVar()
label_2 = Label(win, text='Paste link here', font='arial 19 bold').place(x=160, y=50)
Entry(win, width=70, textvariable=link).place(x=30, y=90)

def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download('c:/Users')
    label_3 = Label(win, text='download', font='arial 15').place(x=180, y=210)

btn = Button(win, text='download', font='arial 15', bg='red', padx=2, command=downloader).place(x=180, y=150)

win.mainloop()




