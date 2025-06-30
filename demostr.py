# streamlit_app.py

import streamlit as st
import datetime
import pandas as pd
import numpy as np


# PAGE CONFIG
st.set_page_config(page_title = "Intro to streamlit", page_icon = "🤩")


#  TEXT SECTION
st.text("good morning")
st.title("Hello, This is My Web Page")
st.write("This is my first Streamlit app.")
st.header("Section Heading")
st.subheader("Sub-heading Example")
st.write("Auto Display of List:", [1, 2, 3])

st.markdown("## INPUT SECTION")


# INPUT FIELDS 
st.text_input("Enter your name:")
st.number_input("Enter a number", min_value=0, max_value=5)
st.text_area("Feedback")

st.date_input(
    "Select Date", 
    min_value=datetime.date(2000, 1, 1), 
    max_value=datetime.date(2027, 12, 31)
)

st.time_input("Select Time")



#  CHOICE WIDGETS
st.checkbox("I agree to the terms")

st.radio("Select your gender:", ["Male", "Female"])
st.selectbox("Select your country:", ["India", "USA"])

# Hobby selection with validation
hobby = st.multiselect(
    "Select your hobbies (Only 2 allowed):", 
    ["Badminton", "Tennis", "Cricket"]
)
done_button= st.button("Done")
if done_button:
    if len(hobby) > 2:
     st.error("❌ Please select only 2 hobbies.")
    elif len(hobby) == 0:
     st.error("❗ Please select at least one hobby.")
    else:
        st.success("✅ Good choice!")


# Sliders
st.slider("How many stars would you give us?", 0, 5)
st.select_slider("Select Difficulty Level:", options=["Easy", "Medium", "Hard"])


# File upload
file1 = st.file_uploader("Upload a CSV file", type=["csv"])
if file1 is None:
    st.warning("⚠️ Please upload a CSV file to continue.")
    st.stop()
else:
    df = pd.read_csv(file1)
    st.success("✅ File uploaded successfully!")
    st.dataframe(df)
    
# BUTTONS 
st.subheader("Button Section")
st.button("Submit the Form")


# SIDEBAR MENU 
st.sidebar.title("🍴 Menu")
st.sidebar.radio(
    "Select your favourite food:",
    ["Rajma Chawal", "Chhole Bhature", "Kadi Chawal"]
)

# file reading (Basic)
button = st.button("Show data")
if button:
    try:
        df = pd.read_csv("students.xls")
        st.dataframe(df)
        shape = df.shape
        st.write("the shape of the data is\n" ,shape)


    except  FileNotFoundError:
        st.error("Sorry no file found")


# CHARTS


# using sample sales data
df = pd.read_csv("sample_sales_data.csv")


  #line chart

st.subheader("Sales & Profit with Time")
st.line_chart(df.set_index('Date')[["Sales", "Profit"]])
 # bar chart
st.subheader("this is the bar chart")
st.bar_chart(df.set_index('Date')[["Sales", "Profit"]])
st.text("the charts are based on this data")
st.dataframe(df)
st.write(df.head())
