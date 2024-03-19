# Global module imports
import streamlit as st

# Local module imports
#from utilities.pyquery import sqlpy

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
st.header("Full Exercise List")

# Query table from database using SQL query, use pyquery module


# Skill Level exercises - Basic, Advanced, Expert
# Exercise name, skill lvl, sets and reps
st.header("Skill Based Exercises")

# Query table from database using SQL query, use pyquery module


# Body Type Exercises - M (Ectomorph, Mesomorph, Endomorph), F (Pear, Apple, Carrot, Celery, Hourglass)
# Exercise name, body type, sex, skill lvl
st.header("Body Type Exercises")

# Query table from database using SQL query, use pyquery module


# Routine maker for different exercises - based on body type, skill, different muscle groups, and/or time spent (exercising/rest)
st.divider()
cont = st.container()

# Add a selectbox to allow users to choose which table they wish to access
exer_conds  = cont.multiselect(
    "Select any categories to generate a routine", 
    ["Full Exercise List", "Skill Based Exercises", "Body Type Exercises"],
    max_selections = 2,
    placeholder = "Choose up to 2 conditions...")

# "Generate Routines" button with select box to generate routines based on selected conditions
cont.button("Generate Routines")

# Function to display an exercise row with its details


# Add an exercise - fill in parameters
st.divider()
