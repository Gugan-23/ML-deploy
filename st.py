import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model2 = joblib.load('brand_to_elements_model.pkl')

# Streamlit UI
st.title("Brand Elements Prediction")

# Input: Brand Name
brand = st.text_input("Enter the Brand Name:")

# If the user provides input
if st.button('Predict'):
    if brand:
        try:
            # Prepare the input for prediction
            input_data = pd.DataFrame({'brand': [brand]})
            st.write(f"Input Data: {input_data}")

            # Make the prediction
            prediction = model2.predict(input_data)
            st.write(f"Prediction Output: {prediction}")

            # Format the response
            response = {
                'Gold (g)': prediction[0][0],
                'Aluminum (g)': prediction[0][1],
                'Silver (g)': prediction[0][2],
                'Carbon (g)': prediction[0][3],
                'Platinum (g)': prediction[0][4],
                'Nickel (g)': prediction[0][5],
                'Lithium (g)': prediction[0][6],
                'Estimated Price (INR)': prediction[0][7]
            }

            # Display the result
            st.write("Predicted Elements and Prices:")
            st.json(response)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    else:
        st.warning("Please enter a valid brand name.")
