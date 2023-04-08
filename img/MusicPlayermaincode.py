import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title("Music Player")
root.geometry("540x690")
root.configure(background='#0f1a2b')
root.resizable(False, False)
mixer.init()

def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

Top_Image = PhotoImage(file="top.png")
Label(root, image=Top_Image, bg="#0f1a2b").place(x=0, y=-210)
 

logo_Image = PhotoImage(file="logo.png")
Label(root, image=logo_Image, bg="#0f1a2b").place(x=145, y=60)



ButtonPlay = PhotoImage(file="play.png")
Button(root, image=ButtonPlay, bg="#0f1a2b", bd=0,
       command=PlayMusic).place(x=225, y=500)

ButtonStop = PhotoImage(file="stop.png")
Button(root, image=ButtonStop, bg="#0f1a2b", bd=0,
       command=mixer.music.stop).place(x=125, y=600)

ButtonResume = PhotoImage(file="resume.png")
Button(root, image=ButtonResume, bg="#0f1a2b", bd=0,
       command=mixer.music.unpause).place(x=225, y=600)

ButtonPause = PhotoImage(file="pause.png")
Button(root, image=ButtonPause, bg="#0f1a2b", bd=0,
       command=mixer.music.pause).place(x=325, y=600)


Menu = PhotoImage(file="menu.png")
Label(root, image=Menu, bg="#0f1a2b").pack(padx=10, pady=200, side=LEFT)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=11, y=210, width=518.7, height=250)

Button(root, text="Open Folder", width=15, height=2, font=("times new roman",
       12, "bold"), fg="Black", bg="#21b3de", command=AddMusic).place(x=13, y=161)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()
