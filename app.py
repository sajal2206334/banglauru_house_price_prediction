import streamlit as st
import pickle
import numpy as np
import sklearn

# Load model and data
model = pickle.load(open('banglore_home_prices_model.pickle', 'rb'))
df = pickle.load(open('bengaluru_home_price_prediction_columns_data.pkl', 'rb'))

# Set the title of the app
st.title("Home Price Prediction")

# Input fields
area = st.number_input('Area (in Square Feet)')
bhk = st.selectbox('BHK', [1, 2, 3, 4, 5])
bathrooms = st.selectbox('Bathrooms', [1, 2, 3, 4, 5])

# Dropdown menu for locations
locations = sorted(df.columns[3:])  # Assuming the first three columns are total_sqft, bath, bhk
location = st.selectbox('Location', locations)

if st.button('Predict Price'):
    # Prepare the input array
    x = np.zeros(len(df.columns) - 1)  # Ensure the length matches the model's expected input
    x[0] = area
    x[1] = bathrooms
    x[2] = bhk

    # Set the location column to 1, ignoring one dummy variable to avoid the trap
    loc_index = df.columns.get_loc(location) - 1
    if loc_index >= 3:  # Adjust index for the dropped dummy variable
        x[loc_index - 1] = 1
    else:
        x[loc_index] = 1

    # Predict price
    prediction = model.predict([x])[0]

    # Display the result
    st.write(f'The predicted price is ₹{prediction:,.2f}')
