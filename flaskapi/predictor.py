import tensorflow as tf
import keras
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# constants
img_width, img_height = 64,64
H5_PATH = "./model.h5"

# config
model = tf.keras.models.load_model('model.h5')



def is_stopSign(path):
    resNum = 0
    img = image.load_img(path, target_size=(img_width, img_height))
    input_arr = image.img_to_array(img)
    input_arr = np.array([input_arr])
    result = model.predict(input_arr)
    res_arr = result[0]

    for n in range(len(res_arr - 1)):
        if res_arr[n] == 1:
            return str(resNum)
        else:
            resNum += 1
