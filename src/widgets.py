import pandas as pd
import numpy as np
import streamlit as st


st.title("Streamlit Text Input")

name = st.text_input("Enter your name")

age = st.slider("Select your age:", 0, 100, 27)

st.write(f"Your age is {age}")

lang_options = ["Python", "Go", "Rust", "Typescript"]

choice = st.selectbox("Choose your favorite programming language:", lang_options)
st.write(f"You selected {choice}")

if name:
    st.write(f"Hello, {name}")


data = {
    "Name": ["John", "Joe", "Jake", "Jill"],
    "Age": [28, 20, 22, 23],
    "City": ["Houston", "New York", "Plantation", "Chicago"]
}

df = pd.DataFrame(data=data)

df.to_csv("sample.csv")

st.write(df)

# chart_data = pd.DataFrame(
#     np.random.randint(0, 100, size=(30, 5)), columns=["a", "b", "c", "d", "e"]
# )

# st.bar_chart(chart_data)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)