# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ni3MRQ8PkGQJwnZJk9kMeFDyyaGaF6wJ
"""
pip 

import tensorflow as tf
import streamlit as st

@st.cache_resource
def load_model():
  model=tf.keras.models.load_model('model.h5')
  return model
model=load_model()
st.write("""
# Bean Leaf Lesion Identifier(Healthy , Angular Leaf Spot, Bean Ruse)"""
)
file=st.file_uploader("Choose an bean leaf photo",type=["jpg","png"])

import cv2
from PIL import Image,ImageOps
import numpy as np

# def import_and_predict(image_data,model):
#     size=(128,128)
#     image=ImageOps.fit(image_data,size,Image.ANTIALIAS)
#     img=np.asarray(image)
#     img_reshape=img[np.newaxis,...]
#     prediction=model.predict(img_reshape)
#     return prediction

import cv2
from PIL import Image, ImageOps
import numpy as np

def import_and_predict(image_data, model):
    size = (128, 128)

    # Resize the image to the expected input shape of the model
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img = cv2.resize(img, (128, 128), interpolation=cv2.INTER_NEAREST)

    # Convert the image to grayscale if necessary
    if img.ndim == 3 and img.shape[2] == 3:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Reshape the image to add a channel dimension
    img_reshape = img.reshape((1,) + img.shape + (1,))

    # Make predictions using the Keras model
    prediction = model.predict(img_reshape)
    return prediction


if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['Healthy, Angular Leaf Spot, Bean Rust']
    string="OUTPUT : "+ class_names[np.argmax(prediction)]
    st.success(string)
