# Streamlit Cheat Sheet

# Import Streamlit library
import streamlit as st
import pandas as pd

# --- Display Text ---
# Display text in various forms
st.text("Display simple text")
st.markdown("# Markdown supported text")
st.header("Header text")
st.subheader("Subheader text")
st.caption("Caption text")

# Display code with optional language syntax highlighting
st.code("print('Hello, Streamlit!')", language='python')

# --- Display Data ---
# Display data in a table format

data_frame = pd.DataFrame({'Column 1': [1, 2, 3, 4],
                           'Column 2': [5, 6, 7, 8],
                           'Column 3': [9, 10, 11, 12],
                           'Column 4': [13, 14, 15, 16]})

st.write("DataFrame:", data_frame)

# Display interactive tables
st.dataframe(data_frame)

# Display static tables
st.table(data_frame)

# --- Widgets: Input ---
# Text input
text_input = st.text_input("Enter some text")

# Number input
number_input = st.number_input("Enter a number")

# Text area for longer text
text_area = st.text_area("Enter multiple lines")

# Date input
date_input = st.date_input("Pick a date")

# Time input
time_input = st.time_input("Pick a time")

# Select a single option
option = st.selectbox("Choose an option", ['Option 1', 'Option 2'])

# Select multiple options
options = st.multiselect("Choose multiple options", ['Option 1', 'Option 2'])

# Slider for selecting a number within a range
slider = st.slider("Choose a number", min_value=0, max_value=10)

# --- Widgets: Buttons and Actions ---
# Button
if st.button("Click Me"):
    st.write("Button clicked!")

# Checkbox
if st.checkbox("Check me out"):
    st.write("Checked!")

# Radio buttons
radio = st.radio("Choose one", ['Option 1', 'Option 2'])

# --- Display Media ---
# Display images
image_url = "https://streamlit.io/images/brand/streamlit-logo-primary-lightmark-lighttext.png"
st.image(image_url)


# --- Layouts and Containers ---
# Columns for side-by-side widgets
col1, col2 = st.columns(2)
with col1:
    st.text_input("Column 1 input")
with col2:
    st.text_input("Column 2 input")

# Expander for collapsible content
with st.expander("See details"):
    st.write("Hidden details")

# --- Display Interactive Charts ---
# Line chart
st.line_chart(data_frame)

# Area chart
st.area_chart(data_frame)

# Bar chart
st.bar_chart(data_frame)


# Note: 'data_frame' should be a pandas DataFrame object containing the data you want to display.
# For images, videos, and audio, you need to provide the file path or URL to the media.
