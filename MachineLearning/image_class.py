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
    img = image.load_img('/Users/aghimire/SE101/clothes/'+train['id'][i],target_size=(400,400,3))
    img = image.img_to_array(img)
    img = img/255
    train_image.append(img)
X = np.array(train_image)
print(X.shape)
plt.imshow(X[2])

y = np.array(train.drop(['id'],axis=1))
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=1)

model = Sequential()
model.add(Conv2D(filters=16, kernel_size=(5, 5), activation="relu", input_shape=(400,400,3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))
model.add(Conv2D(filters=32, kernel_size=(5, 5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))
model.add(Conv2D(filters=64, kernel_size=(5, 5), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))
model.add(Conv2D(filters=64, kernel_size=(5, 5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='sigmoid'))

print(model.summary()) 

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=12, validation_data=(X_test, y_test), batch_size=64)

model.save("model.h5")
print("Saved Model!!")
"""
img = image.load_img('GOT.jpg',target_size=(400,400,3))
img = image.img_to_array(img)
img = img/255

classes = np.array(train.columns[2:])
proba = model.predict(img.reshape(1,400,400,3))
top_2 = np.argsort(proba[0])[:-3:-1] #changed to -3
li = {0}
for i in li:
    print("{}".format(classes[top_2[i]])+" ({:.2})".format(proba[0][top_2[i]]))
plt.imshow(img)
"""
