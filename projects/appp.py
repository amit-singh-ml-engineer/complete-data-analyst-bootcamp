import streamlit as st
import pickle
import pandas as pd
import os

# Page configuration
st.set_page_config(
    page_title="🐟 Fish Weight Prediction",
    page_icon="🐟",
    layout="wide"
)

# Load files
BASE_DIR = os.path.dirname(__file__)

model = pickle.load(open(os.path.join(BASE_DIR, "fish_model.pkl"), "rb"))
scaler = pickle.load(open(os.path.join(BASE_DIR, "scaler.pkl"), "rb"))
encoder = pickle.load(open(os.path.join(BASE_DIR, "encoder.pkl"), "rb"))

# Title
st.title("🐟 Fish Weight Prediction App")
st.markdown("### Predict the weight of a fish using machine learning")

# Sidebar
st.sidebar.header("About")
st.sidebar.info(
    """
    This app predicts fish weight based on:

    - Species
    - Length1
    - Length2
    - Length3
    - Height
    - Width
    """
)

# Species selection
species = st.selectbox(
    "Select Species",
    ['Bream', 'Parkki', 'Perch', 'Pike', 'Roach', 'Smelt', 'Whitefish']
)

# Input columns
col1, col2 = st.columns(2)

with col1:
    length1 = st.number_input("Length1", min_value=0.0)
    length2 = st.number_input("Length2", min_value=0.0)
    length3 = st.number_input("Length3", min_value=0.0)

with col2:
    height = st.number_input("Height", min_value=0.0)
    width = st.number_input("Width", min_value=0.0)

# Predict button
if st.button("Predict Weight"):

    species_encoded = encoder.transform([[species]]).toarray()

    input_df = pd.DataFrame(
        [[length1, length2, length3, height, width]],
        columns=['Length1', 'Length2', 'Length3', 'Height', 'Width']
    )

    species_df = pd.DataFrame(
        species_encoded,
        columns=encoder.get_feature_names_out(['Species'])
    )

    final_input = pd.concat([input_df, species_df], axis=1)
    final_input_scaled = scaler.transform(final_input)

    prediction = model.predict(final_input_scaled)

    st.success(f"🐠 Predicted Fish Weight: {prediction[0]:.2f} grams")

st.markdown("---")
st.caption("Created by Amit Kumar Singh 🚀")