import streamlit as st
import pandas as pd
import joblib


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Aquaculture Water Quality Prediction",
    page_icon="🐟",
    layout="centered"
)


# ==========================================
# LOAD MODEL
# ==========================================

@st.cache_resource
def load_model():

    model = joblib.load("best_model.pkl")
    features = joblib.load("selected_features.pkl")

    return model, features


model, selected_features = load_model()


# ==========================================
# TITLE
# ==========================================

st.title("🐟 Aquaculture Water Quality Prediction")

st.write(
    "Enter the water parameters below to predict "
    "the Water Quality Index."
)

st.divider()


# ==========================================
# INPUTS
# ==========================================

dissolved_oxygen = st.number_input(
    "Dissolved Oxygen",
    min_value=0.0,
    max_value=20.0,
    value=5.0,
    step=0.1
)


ph = st.number_input(
    "pH Levels",
    min_value=0.0,
    max_value=14.0,
    value=7.0,
    step=0.1
)


ammonia = st.number_input(
    "Ammonia Concentration",
    min_value=0.0,
    value=0.5,
    step=0.01
)


nitrite = st.number_input(
    "Nitrite Concentration",
    min_value=0.0,
    value=0.5,
    step=0.01
)


tss = st.number_input(
    "Total Suspended Solids",
    min_value=0.0,
    value=50.0,
    step=0.1
)


# ==========================================
# PREDICTION BUTTON
# ==========================================

if st.button(
    "🔮 Predict Water Quality Index",
    use_container_width=True
):

    input_data = pd.DataFrame({

        "Dissolved Oxygen": [
            dissolved_oxygen
        ],

        "pH Levels": [
            ph
        ],

        "Ammonia Concentration": [
            ammonia
        ],

        "Nitrite Concentration": [
            nitrite
        ],

        "Total Suspended Solids": [
            tss
        ]

    })


    # Make sure column order is exactly
    # the same as training

    input_data = input_data[selected_features]


    # ==========================================
    # PREDICTION
    # ==========================================

    prediction = model.predict(input_data)[0]


    # ==========================================
    # RESULT
    # ==========================================

    st.success(
        f"Predicted Water Quality Index: {prediction:.2f}"
    )


    # ==========================================
    # SIMPLE INTERPRETATION
    # ==========================================

    st.subheader("Water Quality Result")

    if prediction < 3:

        st.error(
            "Poor Water Quality"
        )

    elif prediction < 4:

        st.warning(
            "Moderate Water Quality"
        )

    else:

        st.success(
            "Good Water Quality"
        )