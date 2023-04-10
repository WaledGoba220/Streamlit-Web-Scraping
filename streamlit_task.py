import streamlit as st
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



# st.write("Hello Streamlit 1111")

# Display Text
st.text("Text")
st.write("Super Function")
st.header("My App")
st.subheader("SubHeader App")
st.title("My Title")
st.markdown("Waled Saied")
st.markdown("***Waled Saied***")


# Interactive Widgets

btn = st.button("Submit")

if btn:
    st.info("Done")


# st.radio("Select",{'1','2','3'})


option = st.radio("Select",{'A','B','C'})
if option == 'A':
    st.warning("A is Selected")
elif option == 'B':
    st.error("B is Selected")
else:
    st.success("C is Selected")



st.checkbox("I Agree")


st.selectbox("select",{"A","B","C","D"})

st.slider("Selected",0,100)

st.select_slider("Select",['A','B','C','D','E'])

st.text_input("Enter Name")

st.text_area('Enter Paragaph')

st.file_uploader("Upload")

st.camera_input("Camera Phot")

st.date_input("Today")

st.time_input("Now")

st.number_input("Num")

st.multiselect("Select",["A","B","C","D"])

st.color_picker("Colors")


# DataFrame
df =sns.load_dataset('taxis')
st.write(df)

st.dataframe(df.head())
st.dataframe(df.sample())


