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
st.header("Exercise Table 1")
st.header("Exercise Table 2")
st.header("Exercise Table 3")