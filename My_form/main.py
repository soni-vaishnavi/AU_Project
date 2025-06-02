
#IMPORTS
import streamlit as st
import datetime as dt
from fav_subj import favorite_sub


st.title("Hello tell us about yourself")

name = st.text_input("enter your name")
age = st.slider("Select your age:", 16, 30)
gender = st.radio("Select gender", ["M", "F"])
dob = st.date_input("Choose your dob",value = dt.date(2010,5,4), min_value = dt.date(2000,1,1), max_value = dt.date(2015,12,31))
hobby = st.multiselect("choose your hobby", ["badminton", "chess", "cricket"])
year = st.selectbox("Enter year", [1,2,3,4])
options = ["Maths", "Python", "Machine learning", "Chemistry", "Physics"]
subject = st.selectbox("Choose your favorite subject please", options)
agree = st.checkbox("All the info provided by me are correct.")

#submit


if st.button("Submit"):
    if agree:
            
            txt= favorite_sub(subject)
            st.markdown(f"✅ **Cudos! Form submitted successfully.**  \n**Message:** {txt}")
    else:
          st.warning("Please confirm!")
