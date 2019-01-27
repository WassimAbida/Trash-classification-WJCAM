import numpy as np


from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator
import cv2

class ImageClassifier(object):

    def __init__(self, batch_size=32, epochs=1, validation_split=0.2, dropout=0.3, input_shape_image=(128, 128)):
        
        
        self.batch_size = batch_size
        self.epochs = epochs
        self.step_per_epoch = 20
        self.input_image_shape = input_shape_image
        self.input_shape = self.input_image_shape + (3,)
        self.dropout = dropout
        self.validation_split = validation_split
        self.model = self._build_model()

    def _transform(self, x):   
        x = x / 255.
        x_resize = cv2.resize(x, self.input_image_shape)
        return x_resize
    
    def data_augmentation(self, X):
        datagen = ImageDataGenerator(
                featurewise_center=True,
                featurewise_std_normalization=True,
                rotation_range=20,
                width_shift_range=0.2,
                height_shift_range=0.2,
                horizontal_flip=True)
        # compute quantities required for featurewise normalization
        # (std, mean, and principal components if ZCA whitening is applied)
        
        datagen.fit(X)
        return datagen

    def fit(self, img_loader):
        nb = len(img_loader)
        X = np.zeros((nb,) + self.input_shape)
        Y = np.zeros((nb, 5))
        
        for i in range(nb):
            x, y = img_loader.load(i)
            X[i] = self._transform(x)
            Y[i, y] = 1
            
        datagen = self.data_augmentation(X)
        
        self.model.fit_generator(datagen.flow(X, Y, batch_size=self.batch_size), steps_per_epoch=self.step_per_epoch, epochs=self.epochs)
     
    def predict_proba(self, img_loader):
        nb = len(img_loader)
        X = np.zeros((nb, 128, 128, 3))
        for i in range(nb):
            X[i] = self._transform(img_loader.load(i))
        return self.model.predict(X)
    
    def _build_model(self):
        
        model = Sequential()


        model.add(Conv2D(32, (3,3), activation=None, input_shape=self.input_shape))
        model.add(Conv2D(32,  (3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(3,3)))
        model.add(Dropout(self.dropout))

        model.add( Conv2D (64,(3,3), activation = 'relu'))
        model.add( Conv2D (64,(3,3), activation = 'relu'))
        model.add( MaxPooling2D ( pool_size =(2,2)))
        model.add(Dropout(self.dropout))
        model.add(Flatten())
        model.add(Dense(256,activation = 'relu'))
        model.add(Dropout(0.5))
        model.add(Dense(5, activation='softmax'))
          
        
        sgd = SGD(lr=0.01, decay=0, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy', optimizer=sgd,metrics=['accuracy'])
        
        return model
