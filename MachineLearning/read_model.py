#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import keras
import pandas as pd
from PIL import Image
from keras.preprocessing import image
from keras.models import Sequential
from keras.models import Model
from keras.models import load_model

def read_model(img_name):
    model = load_model('model.h5')
    #print("LOADED model")
    img = image.load_img(img_name)
    img = img.resize((400,400))
    img = image.img_to_array(img)
    img = img/255

    #print("loaded image")

    train = pd.read_csv('outfitCSV.csv')
    #print(train.columns)

    classes = np.array(train.columns[1:])
    #print("classes done")
    proba = model.predict(img.reshape(1,400,400,3))
    #print("proba done")
    best = np.argsort(proba[0])[:-3:-1]
    #print("best done")
    li = {0}
    #print("before")
    #for i in li:
    if classes[best[0]] == 1:
        print("That's a top!")
        return 0
    else:
        print("That's a pair of pants!")
        return 1
    #print("{}".format(classes[best[0]])+" ({:.2})".format(proba[0][best[0]]))
    #plt.imshow(img)
    #print("after")

