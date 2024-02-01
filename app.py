import streamlit as st

# Set page config to apply customizations
st.set_page_config(page_title="PRICE Scoring App", layout="wide")

# Title and introduction
st.title("PRICE Scoring App")
st.markdown("""
This app calculates the PRICE score for your project, incorporating Passion into the traditional RICE framework with adjusted parameters.
""")

# User input fields
with st.form("price_form"):
    passion = st.slider("Passion", min_value=0.0, max_value=10.0, value=0.0, step=0.1, format="%.1f", help="The level of passion or enthusiasm you have for the project (scale of 0 to 10).")
    reach = st.number_input("Reach", min_value=0, format="%d", help="The number of people you believe your project will impact during one calendar year.")
    impact = st.number_input("Impact ($)", min_value=0.0, format="%.2f", help="The projected dollar amount of revenue or cost savings during one calendar year.")
    confidence = st.slider("Confidence", min_value=0.0, max_value=1.0, value=0.1, step=0.1, format="%.1f", help="Your confidence in the estimates, from 0 (least confident) to 1 (most confident), in tenth increments.")
    headcount = st.number_input("Headcount", min_value=0, format="%d", help="Number of people required.")
    months = st.number_input("Months", min_value=0, format="%d", help="Number of months required.")
    submit_button = st.form_submit_button(label="Calculate PRICE Score")

# Calculate and display the PRICE score
if submit_button:
    effort = headcount * months  # Calculate effort based on headcount and months
    if effort <= 0:  # Avoid division by zero
        st.error("Effort must be greater than 0!")
    else:
        price_score = ((reach * impact * confidence * passion) / 100000000) / effort
        st.metric(label="Your PRICE Score is", value=f"{price_score:.1f}")
