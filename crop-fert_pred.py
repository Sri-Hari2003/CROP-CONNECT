import pandas as pd
import pickle

# Load the trained models from pickle files
with open('crop_model.pkl', 'rb') as f:
    crop_model = pickle.load(f)

with open('fertilizer_model.pkl', 'rb') as f:
    fertilizer_model = pickle.load(f)

# Take NPK values input from the user
n, p, k = map(int, input("Enter N, P, K values separated by space: ").split())

# Create new data with NPK values
new_data_crop = [[n, p, k, 21, 82, 7, 203]]  # Example data for crop prediction
new_data_fertilizer = [[n, p, k]]  # Example data for fertilizer prediction

# Predict the crop and fertilizer
predicted_crop = crop_model.predict(new_data_crop)
predicted_fertilizer = fertilizer_model.predict(new_data_fertilizer)

print("Predicted Crop:", predicted_crop)
print("Predicted Fertilizer:", predicted_fertilizer)
