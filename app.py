# app.py

import streamlit as st

# Set page config to apply customizations
st.set_page_config(page_title="PRICE Scoring App", layout="wide")

# Custom theme for Material Design aesthetics
st.write('<style>div.block-container{padding-top:2rem;} div.streamlit-expanderHeader{font-size: large;}</style>', unsafe_allow_html=True)

# Title and introduction
st.title("PRICE Scoring App")
st.markdown("""
This app calculates the PRICE score for your project, incorporating Passion into the traditional RICE framework.
""")

# User input fields
with st.form("price_form"):
    reach = st.number_input("Reach", min_value=0, value=0, help="The number of people you believe your project will impact.")
    impact = st.number_input("Impact", min_value=0, value=0, help="The impact level of your project, typically on a scale from 0.1 to 10.")
    confidence = st.number_input("Confidence", min_value=0, max_value=100, value=100, help="How confident are you in your impact and reach estimates? (0-100%)")
    effort = st.number_input("Effort", min_value=0, value=0, help="The total amount of work required (in person-months).")
    passion = st.number_input("Passion", min_value=0, value=0, help="The level of passion or enthusiasm you have for the project (scale of 0.1 to 10).")
    submit_button = st.form_submit_button(label="Calculate PRICE Score")

# Calculate and display the PRICE score
if submit_button:
    if effort <= 0:  # Avoid division by zero
        st.error("Effort must be greater than 0!")
    else:
        price_score = (reach * impact * confidence * passion) / (effort * 100)  # Adjusted formula to include Passion
        st.metric(label="Your PRICE Score is", value=f"{price_score:.2f}")

