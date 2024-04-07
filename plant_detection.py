import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load the saved model
model = tf.keras.models.load_model('plant_disease_model.h5')

# Get the list of subfolder names (disease names)
subfolder_names = sorted(os.listdir('C:/Users/S Sri Hari/mithack/PlantVillage'))

# Function to preprocess the input image
def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Function to predict the subfolder name (disease name) of the image
def predict_disease(image_path):
    img_array = preprocess_image(image_path)
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions)
    predicted_subfolder_name = subfolder_names[predicted_class_index]
    return predicted_subfolder_name

# Example usage
image_path = 'plant_disease.jpg'  # Replace with the path to your image
predicted_subfolder_name = predict_disease(image_path)
print('Predicted subfolder name:', predicted_subfolder_name)
