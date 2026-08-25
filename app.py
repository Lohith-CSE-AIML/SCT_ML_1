import streamlit as st
import pandas as pd
import joblib


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)


# ---------------- LOAD MODEL ----------------

model=joblib.load("model/House_price_linear_regression.pkl")

# ---------------- TITLE ----------------

st.title("🏠 House Price Prediction")

st.write("Enter the house details below to predict the estimated sale price.")

# ---------------- USER INPUTS ----------------

gr_liv_area=st.number_input(
    "Living Area(sq ft)",
    min_value=100,
    max_value=10000,
    value=2000,
    step=50
)

bedrooms=st.number_input(
    "Number of Bedrooms",
    min_value=0,
    max_value=10,
    value=3,
    step=1
)

bathrooms=st.number_input(
    "Number of Bathrooms",
    min_value=0,
    max_value=10,
    value=2,
    step=1
)

# ---------------- PREDICTION ----------------

if st.button("Predict House Price"):
    input_data=pd.DataFrame(
        {
            "GrLivArea":[gr_liv_area],
            "BedroomAbvGr":[bedrooms],
            "FullBath":[bathrooms]
        }
    )

    prediction_usd = model.predict(input_data)[0]

    # Approximate USD to INR conversion
    usd_to_inr = 88

    prediction_inr = prediction_usd * usd_to_inr

    st.success(
        f"Estimated House Price: ₹{prediction_inr:,.2f}(Indian Rupees)"
    )

    st.success(
        f"Estimated House Price: ${prediction_usd:,.2f} (US Dollars)"
    )



# ---------------- INFORMATION ----------------

st.info(
    "This model was trained using GrLivArea, BedroomAbvGr, "
    "and FullBath features from the Ames Housing dataset."
)