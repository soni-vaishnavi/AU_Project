import streamlit as st
import datetime
from PIL import Image

# TEXT
st.title("hello this is my web page")
st.write("this is my first streamlit app")
st.header("it is section heading")
st.subheader("this is the sub heading")
st.write("Auto display:", [1, 2, 3])

st.markdown("_**INPUT SECTION**_")

st.text_input("Enter your name ")
st.number_input("enter the number",min_value = 0, max_value = 25)
st.text_area("Feedback")


#st.date_input("Select date")
st.date_input("select date ",min_value= datetime.date(2000,1,1), max_value = datetime.date(2027,12,31) )

st.time_input("select time")

#BOXES
st.checkbox("I agree")
st.radio("Select your gender", ["Male", "Female"])
st.selectbox("Country", ["India", "USA"])
hobby = st.multiselect("select your hobby (only 2 please)", ["badminton", "tennis", "cricket"])     
if len(hobby)> 2:
    st.error("choose only 2 please")
elif len(hobby)== 0:
    st.error("please select atleast one value")
else:
    st.success("good choice")
st.slider("how many stars will you give us", 0,5)
st.select_slider("Difficulty", options = ["easy", "medium", "hard"])
st.file_uploader("upload a csv file please")


st.subheader("buttons")

st.button("submit the form")


st.sidebar.title("Menu")
st.sidebar.radio("select your fav. food:", ["rajma chawal", "chhole bhature", "kadi-chawal"])

st.subheader("IMAGE SECTION")

upload_image = st.file_uploader("upload an image", type = ["jpg", "jpeg", "png"])

if upload_image is not None:
    image = Image.open(upload_image)

    st.image(image, caption = "nice image")
    st.success("uploaded successfully")
 