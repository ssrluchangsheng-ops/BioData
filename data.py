import streamlit as st
from PIL import Image

st.title("Luuu")

st.header("About Me")

image = Image.open("LUU.jpg")
st.image(image,caption="My Profile Picture", width=250)

st.text("1.I am a student")
st.text("2.I am from China")
st.text("3.I want to sleep ")

st.success("Welcome to my first Streamlip app!")