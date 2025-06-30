import streamlit as st
import datetime as dt
import pandas as pd

# setting the config
st.set_page_config(page_title = "streamlit lecture", page_icon = "🤩")
# text

st.title("this is intro of streamlit")
st.text("Good Morning!")
st.header("this is the header")
st.subheader("this is the subheader")
st.write("using the write function")

st.write("displaying the list", [1,2,4,8])

st.markdown("# this is the markdown")

st.markdown("## this is the markdown")
st.markdown("### this is the markdown")


# USER INPUT

st.text_input("enter your name")
st.number_input("enter your age", min_value = 18, max_value = 25)

#date input

st.date_input(
    "Select your DOB",
    value = dt.date(2005,5,4),
    min_value = dt.date(2001,1,1),
    max_value = dt.date(2010,12,31)
)

st.time_input("select time")

# choice widgets

st.radio("select your fav colour", ["blue", "red", "pink"])
st.selectbox("select your game", ["cricket", "tennis","football"])
sub = st.multiselect("choose your fav subject", ["python", "chemistry", "maths"])
done = st.button("done")
if done:
     if len(sub)>2:
          st.warning("select only 2 subjects")
     elif len(sub)==0:
          st.error("select atleast one value")
     else:
          st.success("thankyou")
     


st.checkbox("I agree")

# sliders
st.slider("how much would you rate us", 0 ,5)
st.select_slider("level",["easy", "moderate","difficult"])

#file uploader

# file= st.file_uploader("upload a csv file", type =['csv'])
# if file is None:

#     st.error("upload file please")
#     st.stop()

# else:
#     df = pd.read_csv(file)
#     st.success("file uploaded")

#     st.dataframe(df.head())

#button


#SIDEBAR

st.sidebar.title("this is the sidebar")
st.sidebar.radio("select the value", ["blue", "green", "red"])


button=st.button("show data")
if button:
    try:
         df = pd.read_csv("students.xls")
         st.dataframe(df)
    except:
         st.write("no file found")

# charts

df2 = pd.read_csv("sample_sales_data.csv")

st.dataframe(df2)

st.line_chart(df2.set_index('Date')[["Sales","Profit"]])

st.bar_chart(df2.set_index('Date')[["Sales","Profit"]])

