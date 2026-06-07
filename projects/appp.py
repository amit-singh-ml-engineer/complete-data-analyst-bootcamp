import streamlit as st
import pickle
import pandas as pd

# Load saved files
import os
import pickle

BASE_DIR = os.path.dirname(__file__)

model = pickle.load(open(os.path.join(BASE_DIR, "fish_model.pkl"), "rb"))
scaler = pickle.load(open(os.path.join(BASE_DIR, "scaler.pkl"), "rb"))
encoder = pickle.load(open(os.path.join(BASE_DIR, "encoder.pkl"), "rb"))

st.title("🐟 Fish Weight Prediction")

species = st.selectbox(
    "Species",
    ['Bream','Parkki','Perch','Pike','Roach','Smelt','Whitefish']
)

length1 = st.number_input("Length1")
length2 = st.number_input("Length2")
length3 = st.number_input("Length3")
height = st.number_input("Height")
width = st.number_input("Width")

if st.button("Predict Weight"):

    species_encoded = encoder.transform([[species]]).toarray()

    input_df = pd.DataFrame(
        [[length1, length2, length3, height, width]],
        columns=['Length1','Length2','Length3','Height','Width']
    )

    species_df = pd.DataFrame(
        species_encoded,
        columns=encoder.get_feature_names_out(['Species'])
    )

    final_input = pd.concat([input_df, species_df], axis=1)

    final_input_scaled = scaler.transform(final_input)

    prediction = model.predict(final_input_scaled)

    st.success(f"Predicted Fish Weight: {prediction[0]:.2f} grams")