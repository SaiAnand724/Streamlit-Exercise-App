# Global module imports
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

# Client exercises, description, skill lvl, body type, muscle groups, sets and reps 
st.header("Client Table 2")

# Client exercises, description, skill lvl, body type, Intensity, 
# muscle groups, sets and reps, time spent exercising per session | (bundles data after a week)
st.header("Client Table 3")

# graphs for different metrics - weight, time spent (exercising/rest), calories (in the future), exercise sets and reps

