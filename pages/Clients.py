# Global module imports
# import utilities
import streamlit as st


# Define the main page title and icon
st.set_page_config(
    page_title="Client Tables"
)

# Display a success message in the sidebar for page selection
st.sidebar.success("Select a page")

# Login section for clients to view their information

# Set the main title of the app
st.title("Client Tables")

# Provide structure for page elements

# Overview of full Client info
# Client name, weight, dob, sex, body type, calorie information (potentially), 
st.header("Client Table 1")
st.text("Full Client Info")

# Query table from database using SQL query, use pyquery module

# Client exercises, description, skill lvl, body type, muscle groups, sets and reps 
st.header("Client Table 2")
st.text("Client Exercises")

# Query table from database using SQL query, use pyquery module


# Client exercises, description, skill lvl, body type, Intensity, 
# muscle groups, sets and reps, time spent exercising per session | (bundles data after a week)
st.header("Client Table 3")
st.text("Client Sessions/Routines")

# Query table from database using SQL query, use pyquery module


# graphs for different metrics - weight, time spent (exercising/rest), calories (in the future), exercise sets and reps
st.divider()
cont = st.container()

# Add a selectbox to allow users to choose which table they wish to access
client_table  = cont.selectbox(
    "Which client table would you like to access?", 
    ('Client Information','Exercises Logged','Sessions/Routines'),
    index = None,
    placeholder = "Select a table...")

# "Graph Table" button with select box to choose which table to graph and display
cont.button("Graph Table")

st.divider()