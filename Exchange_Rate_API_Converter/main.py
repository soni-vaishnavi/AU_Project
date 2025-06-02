import streamlit as st
from exchange_api import exchange_rate

# creating the streamlit code to design a GUI Interface for the basic web app

st.set_page_config(page_title="Currency Converter", page_icon= "💸")

st.title = "Currency to INR Converter"
st.write("Please select the currency you need to convert:")

currency_options = ["USD", "AED", "CAD", "EUR", "GBP", "AUD", "SGD", "JPY", "IMP"]

selected_curr = st.selectbox("Choose a currency:",currency_options)

if st.button("Convert to INR:"):
    INR_VAL= exchange_rate(selected_curr) #calling the function here
    if INR_VAL:
     st.success(f"1{selected_curr} = Rs. {INR_VAL}")
    else:
     st.error("Please try again later")