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
st.header("Exercise Table 1")
st.text("Full Exercise List")

# Query table from database using SQL query, use pyquery module
# full_exerc_tbl = dbse.sqlpy('''SELECT * FROM exercise_list; ''')
# full_exerc_tbl = [["Bench Press", "Moderate", "Chest"], ["Incline Bench Press", "Very High", "Triceps"]], ...


# Skill Level exercises - Basic, Advanced, Expert
# Exercise name, skill lvl, sets and reps
st.header("Exercise Table 2")
st.text("Skill Based Exercises")

# Query table from database using SQL query, use pyquery module
# skill_exerc_tbl = dbse.sqlpy('''SELECT * FROM skill_based WHERE skill_lvl= ['Basic', 'Advanced', 'Expert']; ''')
# skills_levels = ["Basic", "Advanced", "Expert"]
# skill_lvl = st.selectbox("Choose a Skill Level: ", skills_levels)


# Body Type Exercises - M (Ectomorph, Mesomorph, Endomorph), F (Pear, Apple, Carrot, Celery, Hourglass)
# Exercise name, body type, sex, skill lvl
st.header("Exercise Table 3")
st.text("Body Type Exercises")

# Query table from database using SQL query, use pyquery module
# bodyt_exerc_tbl = dbse.sqlpy('''SELECT * FROM bodytype_exercises WHERE sex=['M' or 'F'] and 
# body_type=[[Ectomorph, Mesomorph, Endomorph] or [Pear, Apple, Carrot, Celery, Hourglass]]; ''')

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
