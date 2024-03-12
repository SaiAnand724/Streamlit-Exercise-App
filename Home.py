# Global module imports
import streamlit as st

# Define the main page title and icon
st.set_page_config(
    page_title = "Exercise App - Home Page"
)

st.title("Home Page")

st.sidebar.success("Select a page")

st.text("Hello World")


# Provide structure for page elements

# streamlit_app.py
#import mysql.connector as sql_conn

st.header("SQL Table")
st.text("Doc Source: https://docs.streamlit.io/knowledge-base/tutorials/databases/mysql")
# Initialize connection.
sqlconn = st.connection('mysql', type='sql')

# Perform query.
df = sqlconn.query('SELECT * from mytable;', ttl=600)

# print query table as dataframe
st.dataframe(df)

# 