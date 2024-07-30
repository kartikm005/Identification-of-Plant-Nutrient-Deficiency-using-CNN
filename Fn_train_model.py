# import the necessary packages
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam

from tensorflow.keras.utils import load_img
from keras_preprocessing.image import img_to_array


from keras.utils import to_categorical
from pyimagesearch.lenet import LeNet
from imutils import paths
##import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
import cv2
import os
from sklearn.model_selection import train_test_split


def train_model():
        # initialize the number of epochs to train for, initia learning rate,
        # and batch size
        EPOCHS = 100
        INIT_LR = 1e-3
        BS = 16

        noofclasses=5

        # initialize the data and labels
        print("loading images...")
        data = []
        labels = []

        # grab the image paths and randomly shuffle them
        imagePaths = sorted(list(paths.list_images("Train")))
        ##random.seed(42)
        ##random.shuffle(imagePaths)


        # loop over the input images
        labelnum=-1
        prev=""
        for imagePath in imagePaths:
                # load the image, pre-process it, and store it in the data list
                image = cv2.imread(imagePath)
                image = cv2.resize(image, (28, 28))
                image = img_to_array(image)
                data.append(image)

                # extract the class label from the image path and update the
                # labels list
                label = imagePath.split(os.path.sep)[-2]
                
                if label != prev:
                        labelnum = labelnum +1
                        prev=label
        ##	print(label,labelnum)
                labels.append(labelnum)

        # scale the raw pixel intensities to the range [0, 1]
        data = np.array(data, dtype="float") / 255.0
        labels = np.array(labels)

        # partition the data into training and testing splits using 75% of
        # the data for training and the remaining 25% for testing
        (trainX, testX, trainY, testY) = train_test_split(data,
                labels, test_size=0.3, random_state=20)

        ##
        ##print(trainY)
        ##print(np.sort(testY))


        # convert the labels from integers to vectors
        trainY = to_categorical(trainY, num_classes=noofclasses)
        testY = to_categorical(testY, num_classes=noofclasses)

        # construct the image generator for data augmentation
        aug = ImageDataGenerator(rotation_range=15, width_shift_range=0.1,
	height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
	horizontal_flip=True, fill_mode="nearest")
        # initialize the model
        print("Compiling model...")
        model = LeNet.build(width=28, height=28, depth=3, classes=noofclasses)
        opt = Adam(learning_rate=INIT_LR, decay=INIT_LR / EPOCHS)
        model.compile(loss="binary_crossentropy", optimizer=opt,
                metrics=["accuracy"])

        # train the network
        print("Training Network...")
        H = model.fit(aug.flow(trainX, trainY, batch_size=BS),
                validation_data=(testX, testY), steps_per_epoch=len(trainX) // BS,
                epochs=EPOCHS, verbose=2)

        # save the model to disk
        print("Storing Model")
        model.save("PL_kb.model")
        print("Training Over")

        accuracy = H.history['accuracy'][-1]


        print('\nValidation Accuracy : ',round(accuracy*100,2),' %')









 


