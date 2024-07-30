from tkinter import *
import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from PIL import Image, ImageTk

from Fn_check_single_case import check_single_case
from Fn_check_all_images import check_all_images

def close1():
    exit(0)

def show_Single_check_single_case():
    Outtxt.delete(1.0,END) 
    out1=check_single_case()
    
    Outtxt.insert(INSERT, out1)

def show_check_all_images():
    Outtxt.delete(1.0,END) 

    print("@@@@@@@@@@@@@@@")
    out1=check_all_images()
    
    
    print("###",out1)
    Outtxt.insert(INSERT, out1)


def start():
    window = Tk()
    window.title("Identification of Plant Nutrient Deficiencies Using CNN ")
    window.geometry('1330x650')

    img = PhotoImage(file="img\\back1.png")
    label = Label(
        window,
        image=img
    )
    label.place(x=0, y=0)

    ##label = tk.Label(window)
    ##img = Image.open(r"back1.jpg")
    ##label.img = ImageTk.PhotoImage(img)
    ##label['image'] = label.img
    ##label.grid(column=0, row=0)

    button = Button(
        window,
        text='@|   Model Training             |',
        relief=RAISED,
        font=('Arial Bold', 18),
        bg="yellow",
        fg="green",
        command=close1
    )
    button.place(x=160, y=150)

    Outtxt = Text(window, height = 23, width = 60,bg="#D0EBCB",fg="blue",font=('Arial Bold', 12))
    Outtxt.config(font =("Arial Bold", 16))
    Outtxt.place(x=540,y=100)

    button = Button(
        window,
        text='@|   Check for Deficiencies |',
        relief=RAISED,
        font=('Arial Bold', 18),
        bg="yellow",
        fg="green",
        command=show_Single_check_single_case
    )
    button.place(x=160, y=150+100)

    button = Button(
        window,
        text='@|   Performane Analysis    |',
        relief=RAISED,
        font=('Arial Bold', 18),
        bg="yellow",
        fg="green",
        command=show_check_all_images
    )
    button.place(x=160, y=150+200)

    button = Button(
        window,
        text='@|                 Close              |',
        relief=RAISED,
        font=('Arial Bold', 18),
        bg="yellow",
        fg="green",
        command=close1
    )
    button.place(x=160, y=150+300)

##window.mainloop()



