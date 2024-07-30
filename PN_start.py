from tkinter import *
import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from PIL import Image, ImageTk

from Fn_check_single_case import check_single_case
from Fn_check_all_images import check_all_images
from Fn_train_model import train_model

import gtts
from playsound import playsound


global prev

prev=0

def close1():
    exit(0)

def prevention():
    global prev
    
    if prev==0:
##        tts1 = gtts.gTTS("First Check for Deficienci",lang='en',tld='co.in')
##        tts1.save("Er.mp3")
        playsound("Er.mp3")
    elif prev==1:
         msg1="Prevention , The Calcium deficiency can be corrected by using solutions\
         1. Rectified by adding agricultural lime to acid soils, aiming at a pH of 6.5, \
         unless the subject plants specifically prefer acidic soil. \
         2. Organic matter should be added to the soil to improve its moisture-retaining \
           capacity"
         #tts1 = gtts.gTTS(msg1,lang='en',tld='co.in')
         #tts1.save("prev1.mp3")
         playsound("prev1.mp3")
    elif prev==2:
         msg1="Prevention , The Iron deficiency can be corrected by using following :\
         1. supplemental iron is by spraying fertilizer on the plant leaves. \
         2. An inexpensive and commonly used material for this purpose is \
         ferrous sulfate (FeSO4. 2H2O). Mix 1 to 2 oz of ferrous sulfate\
           in 1 gallon of water."
         #tts1 = gtts.gTTS(msg1,lang='en',tld='co.in')
         #tts1.save("prev2.mp3")
         playsound("prev2.mp3")

    elif prev==3:
         msg1="Prevention ,  The Potassium deficiency can be corrected by using following:\
1, Spread organic mulch beneath plants and apply potassium fertilizer, \
2, preferably slow-release forms such as potassium silicate or \
   sulfur- or polymer-coated potassium products. \
3, Potassium sulfate may be used, and potassium will be held by \
   organic matter and clay particles."
         #tts1 = gtts.gTTS(msg1,lang='en',tld='co.in')
         #tts1.save("prev3.mp3")
         playsound("prev3.mp3")

    elif prev==4:
         msg1="Prevention , The phosphorus deficiency can be corrected by using following:\
1, Make pH adjustment.\
2, Flush plants with pH water and nutrients containing phosphorus.\
3, Do not overwater plants.\
4, Ensure the temperature is correct.\
5, Provide plants with the correct nutrient ratio.\
6, Change out the reservoir."

         #tts1 = gtts.gTTS(msg1,lang='en',tld='co.in')
         #tts1.save("prev4.mp3")
         playsound("prev4.mp3")


         












               
    

def saycouse(out1):
    global prev
    
    if "Calcium" in out1:
        prev=1
        playsound("1.mp3")
    elif "Iron" in out1:
        playsound("2.mp3")
        prev=2
    elif "Potassium" in out1:
        playsound("3.mp3")
        prev=3
    elif "phosphorus" in out1:
        playsound("4.mp3")
        prev=4
    
def show_Single_check_single_case():
    Outtxt.delete(1.0,END) 
    out1=check_single_case()
    
    Outtxt.insert(INSERT, out1)
    Outtxt.update()

    saycouse(out1)
    

def show_check_all_images():
    Outtxt.delete(1.0,END) 

    print("@@@@@@@@@@@@@@@")
    out1=check_all_images()
    
    
    print("###",out1)
    Outtxt.insert(INSERT, out1)


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
    width=25,
    command=train_model
)
button.place(x=120, y=150)

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
    width=25,
    command=show_Single_check_single_case
)
button.place(x=120, y=150+100)

button = Button(
    window,
    text='@|       Prevention        |',
    relief=RAISED,
    font=('Arial Bold', 18),
    bg="yellow",
    fg="green",
    width=25,
    command=prevention
)
button.place(x=120, y=150+200)


button = Button(
    window,
    text='@|   Performane Analysis    |',
    relief=RAISED,
    font=('Arial Bold', 18),
    bg="yellow",
    fg="green",
    width=25,
    command=show_check_all_images
)
button.place(x=120, y=150+300)

button = Button(
    window,
    text='@|                 Close              |',
    relief=RAISED,
    font=('Arial Bold', 18),
    bg="yellow",
    fg="green",
    width=25,
    command=close1
)
button.place(x=120, y=150+400)

##window.mainloop()



