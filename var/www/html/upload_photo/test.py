import numpy as np
import tensorflow
from tensorflow import keras
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.applications import imagenet_utils
#from sklearn.metrics import confusion_matrix
##from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D, GlobalAveragePooling2D, AveragePooling2D
from tensorflow.keras.applications.mobilenet import preprocess_input
import itertools
import os
import shutil
import random
#import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import argparse
import sys


model =load_model("/var/www/html/upload_photo/mango_behavior14.h5")
#model.summary()

def prepare_image(image_path, show=True):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    if show:
        display(Image(filename=image_path))
        return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)


def mobile_cl(image_path, show=True):
    prepared = prepare_image(image_path, show)
    ans = mobile.predict(prepared)
    return imagenet_utils.decode_predictions(ans)

parser = argparse.ArgumentParser()
parser.add_argument('file_path', type = str)
args = parser.parse_args()
fp = args.file_path

img = image.load_img(fp, target_size=(224, 224))
img_tensor = image.img_to_array(img)
img_tensor=np.expand_dims(img_tensor,axis=0)
img_tensor/=255.

cls_list = ['其他','授粉不全','果實 炭疽病','果實 黑斑病','果實(未成熟)','果實成熟','白龜神','紅斑炭疽病','紅蜘蛛','缺朋 缺鈣','葉子','葉子 百粉病','葉蟬','葉部 黑斑病或炭疽病','蒂腐病 果實','薊馬 果實','藻斑病','檬果壯鋏普癭蚋','鑽心蟲']


x = image.img_to_array(img)
x = np.expand_dims(x, axis = 0)

pred = model.predict(x)[0]
prediction=model.predict(img_tensor)
pre_y=np.array(prediction)
print('{:2.2f}%'.format(pre_y.max()*100))

