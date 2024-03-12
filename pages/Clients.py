# Global module imports
import streamlit as st

# Define the main page title and icon
st.set_page_config(
    page_title="Client Tables"
)

# Display a success message in the sidebar for page selection
st.sidebar.success("Select a page")

# Set the main title of the app
st.title("Client Tables")

# Provide structure for page elements
st.header("Client Table 1")
st.header("Client Table 2")
st.header("Client Table 3")