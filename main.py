import streamlit as st
import tensorflow as tf
import cv2
from PIL import Image, ImageOps
import numpy as np

@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('dog_model.h5')
    return model

model = load_model()

st.write("# Dog Breed Classification System by Jay Merie Ann Bugarin")

file = st.file_uploader("Choose any dog photo from computer", type=["jpg", "png"])

def import_and_predict(image_data, model):
    size = (244, 244)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis, ...]
    prediction = model.predict(img_reshape)
    return prediction

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    class_names = ['African hunting dog','Chow Chow','French bulldog','German shepherd','Pomeranian','Poodle','Pug', 'Rottweiler', 'Tibetan mastiff', 'Yorkshire terrier']
    string = "OUTPUT: " + class_names[np.argmax(prediction)]
    st.success(string)
