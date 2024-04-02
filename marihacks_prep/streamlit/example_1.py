"""
Building a simple website that asks for the user's name and greets them
"""

# Import the streamlit library
import streamlit as st

# Title of the web app
st.title('Welcome to your first Streamlit App')

# Markdown text can be used to add descriptions or instructions
st.markdown('Please enter your name in the input box below:')

# Text input widget for the user to enter their name
user_name = st.text_input('Name')

# Button to submit the name. If the button is clicked, it returns True.
if st.button('Submit'):
    # This block runs when the user clicks the 'Greet me!' button
    # Display a greeting message using the provided name
    st.write(f'Hello, {user_name}! You made your first Streamlit app.')

# Instructions to run:
# Open a terminal, navigate to the directory containing the file, and run:
# streamlit run <file_name>
# Your default web browser will open a new tab displaying the app.
