"""
Building a simple task list with Streamlit
"""

# Import the streamlit library for web app development
import streamlit as st

# Define a function to manage task operations (add, view, clear)


def task_manager():
    # Use Streamlit's session state to store tasks if it doesn't already exist
    if 'tasks' not in st.session_state:
        st.session_state['tasks'] = []

    # Create a form for task input
    with st.form("Task Form", clear_on_submit=True):
        # Text input for a new task
        new_task = st.text_input("Enter a task", "")
        # Submit button for the form
        submitted = st.form_submit_button("Add Task")
        if submitted and new_task:  # Check if the form is submitted and the input is not empty
            # Add the new task to the list of tasks
            st.session_state['tasks'].append(new_task)

    # Display the current list of tasks
    if st.session_state['tasks']:
        st.write("### Current Tasks")
        for i, task in enumerate(st.session_state['tasks'], start=1):
            st.write(f"{i}. {task}")
    else:
        st.write("No tasks added yet.")

    # Button to clear all tasks
    if st.button("Clear Tasks"):
        st.session_state['tasks'] = []  # Clear the list of tasks


# Title of the web app
st.title('Task List App')

# Instructions
st.write("Add and manage your tasks.")

# Call the task manager function to handle task operations
task_manager()
