import streamlit as st
import pandas as pd
import numpy as np

# Title of the application
st.title("Hello Streamlit")

# Display a text
st.write("This is a simple text")

# Create a dataframa
d = {
    "first column": [1, 2, 3, 4],
    "second_column": [10, 20, 30, 40]
}

df = pd.DataFrame(data=d)

# Display the dataframe
st.write("here is the dataframe")
st.write(df)

# Create a line chart
chart_data = pd.DataFrame(
    np.random.randint(0, 100, size=(20, 4)), columns=["a", "b", "c", "d"]
)

st.line_chart(chart_data)
