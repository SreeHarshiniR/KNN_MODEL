import streamlit as st

st.set_page_config(page_title="My Streamlit App", layout="centered")

st.title("🚀 My First Streamlit App")
st.write("Welcome to my Streamlit application!")

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120)

if st.button("Submit"):
    st.success(f"Hello {name}! You are {age} years old.")

st.sidebar.header("About")
st.sidebar.info("This is a basic Streamlit app.")
