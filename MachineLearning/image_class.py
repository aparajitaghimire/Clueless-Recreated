#!/usr/bin/env python3 

import tensorflow as tf
import keras
import PIL 
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
from keras.preprocessing import image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tqdm import tqdm


train = pd.read_csv('outfitCSV.csv')   
print(train.head())
print(train.columns)

train_image = []
for i in tqdm(range(train.shape[0])):
    img = image.load_img('/home/pi/OutfitRaspberryPi/clothes/'+train['id'][i],target_size=(400,400,3))
    img = image.img_to_array(img)
    img = img/255
    train_image.append(img)
print("hihi")
X = np.array(train_image)
print(X.shape) 
print("hi")


