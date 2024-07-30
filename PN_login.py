from tkinter import *
import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3 as sql
import os 


#pppp 1111
def close1():
    exit(0)

def  login():

    username = Outtxt1.get("1.0",'end-1c')

    password = Outtxt2.get()
    
    con = sql.connect("plant.db")
    cur = con.cursor()
    statement = f"SELECT username from sysuser WHERE username='{username}' AND Password = '{password}';"
    cur.execute(statement)
    if not cur.fetchone():  # An empty result evaluates to False.
        messagebox.showinfo("Error ","Login failed")
    else:
        messagebox.showinfo("Welcome","Valid")
        ##os.system("PN_start.py 1")
        window.destroy()
        PN_start
        



        
##
##    try:
##        print(statement)
##        stat=cur.fetchall()[0]
##        print(stat)
##        messagebox.showinfo("Login ","Valied User")
##        execfile("PN_start.py")
##        
##    except:
##        
##        report="Invalid User"
##        messagebox.showinfo("Error ",report)

    
    

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


head1 = Label(window, 
             text = "Username : ",
             font=('Arial', 16),
             )

head1.place(x = 160,y = 200)

Outtxt1 = Text(window, height = 1, width = 20)
Outtxt1.config(font =("Arial Bold", 18))
Outtxt1.place(x=300,y=200)


head2 = Label(window, 
             text = "Password : ",
             font=('Arial', 16),
             )

head2.place(x = 160,y = 300)

Outtxt2 = Entry(window)
Outtxt2.config(font =("Arial Bold", 18))
Outtxt2.config(show="*");

Outtxt2.place(x=300,y=300)



button = Button(
    window,
    text='   Login  ',
    relief=RAISED,
    font=('Arial Bold', 18),
    bg="yellow",
    fg="green",
    command=login
)
button.place(x=260, y=400)




##window.mainloop()



