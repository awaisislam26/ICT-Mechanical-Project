import streamlit as st

# Application Title
st.title("Mechanical Engineering Calculation Tool")

# User Input via Sidebar
st.sidebar.header("Input Parameters")
val = st.sidebar.number_input("Enter Value (e.g., Mass in kg)", value=1.0)

# Engineering Logic
gravity = 9.81
weight = val * gravity

# Output Display
st.header("Results")
st.success(f"The calculated Weight is: {weight:.2f} Newtons")
