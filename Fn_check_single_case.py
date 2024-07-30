# import the necessary packages
from keras_preprocessing.image import img_to_array

from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
import tkinter as tk
from tkinter import filedialog
import glob
from tkinter import messagebox
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from scipy import interp
from itertools import cycle
from playsound import playsound

def check_single_case():
    
    def_label=['Healty','Calcium Deficiency','Iron Deficiency','Potassium Deficiency','Phosphorus Deficiency']

    # load the trained convolutional neural network
    print("Load Model ...")
    model = load_model('PL_kb.model')

    root = tk.Tk()
    root.withdraw()
    imgfile = filedialog.askopenfilename(initialdir = "test",title = "Select Image",filetypes = (("Img files","*.jpg"),("all files","*.*")))

    # load the image
    image = cv2.imread(imgfile)  
     

    im1 = cv2.resize(image, (400, 300))               
    cv2.imshow("Selected Image", im1)
    cv2.waitKey(1)

    # pre-process the image for classification
    image = cv2.resize(image, (28, 28))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # classify the input image
    P = model.predict(image)

    maxindex = P.argmax()

    Plabel=def_label[maxindex]

    print("\nImage Predicted As ",Plabel)

    playsound(Plabel+".mp3")

    messagebox.showinfo("Classified As ",Plabel)


    
    Couse ="" 
    match maxindex:
        case  1:

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Ca (Calcium) deficiency causes : ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
            print("##  Acidic, sandy, or coarse soils often contain less calcium ")
            print("##  Uneven soil moisture and overuse of fertilizers")
            print("##  At times, even with sufficient calcium in the soil,\n        it can be in an insoluble form and is then unusable by the\n        plant or it could be attributed to a transport protein")

##            msg1="Calcium deficiency causes : "+ \
##            "1.  Acidic, sandy, or coarse soils often contain less calcium "+\
##            "2.  Uneven soil moisture and overuse of fertilizers"+\
##            "3.  At times, even with sufficient calcium in the soil,\n        it can be in an insoluble form and is then unusable by the\n        plant or it could be attributed to a transport protein"

        
            #tts1 = gtts.gTTS(msg1,lang='en',tld='co.in')
            #tts1.save("1.mp3")
            ##playsound("1.mp3")


            f = open("ca.txt", "r")
            Couse=f.read()

        case  2:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Fe (Iron)  deficiency causes   :")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
             
            print("##  Iron deficiency is also common when soils are cool")
            print("##  high in calcium, poorly drained, or waterlogged and when root\n      health is impaired by root decay pathogens, nematodes, \n       or other biological or physical causes")

            f = open("Fe.txt", "r")
            Couse=f.read()

        case  3:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("K  (Potassium) deficiency causes :")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            print("##    aeration deficit, compaction, high soil pH (especially with plants adapted to acidic soil),\n      inappropriate irrigation, mechanical (physical) injury to roots,\n      poor drainage (waterlogging),\n     root decay pathogens, and root-feeding nematodes")

            f = open("K.txt", "r")
            Couse=f.read()
            
        case   4:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("P (Phosphorus) deficiency causes :")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            print("Causes are soil or root problems as described for nitrogen deficiency\n      that prevent roots from adequately absorbing phosphorus.\n      Certain herbicides also cause leaf distortion and curling \n        that can resemble phosphorus deficiency symptoms")

            f = open("P.txt", "r")
            Couse=f.read()
            
    return Couse



##check_single_case()




