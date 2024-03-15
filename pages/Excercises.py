# Global module imports
import streamlit as st

# Define the main page title and icon
st.set_page_config(
    page_title="Exercises Tables"
)

# Display a success message in the sidebar for page selection
st.sidebar.success("Select a page")

# Set the main title of the app
st.title("Exercise Tables")

# Provide structure for page elements

# Overview of Full Exercise list
# Exercise name, intensity, muscle groups, skill lvl, descriptions
st.header("Exercise Table 1")

# Skill Level exercises - Basic, Advanced, Expert
# Exercise name, skill lvl, sets and reps
st.header("Exercise Table 2")

# Body Type Exercises - M (Ectomorph, Mesomorph, Endomorph), F (Pear, Apple, Carrot, Celery, Hourglass)
# Exercise name, body type, sex, skill lvl
st.header("Exercise Table 3")

# Function to display an exercise row with its details

# Add an exercise - fill in parameters
