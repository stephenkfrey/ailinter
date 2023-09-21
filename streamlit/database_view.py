import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="Mapping Demo", page_icon="🌍", layout="wide")

st.markdown("# Mapping Demo")
st.sidebar.header("Mapping Demo")
st.write(
    """This demo shows how to use
[`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
to display geospatial data."""
)

def database_view_page():
    # New code for loading and displaying the SQLite database
    conn = sqlite3.connect('../test_db.db')
    query = "SELECT * FROM messages"  # Replace with your table name
    df = pd.read_sql_query(query, conn)

    df['response'] = df['response'].str.replace('\n', '<br>')

    # Define CSS to control column widths
    css = """
    <style>
    table.dataframe td {
        vertical-align: top;
        font-size: 18px; 
    }
    </style>
    """

    # Apply CSS and display DataFrame
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)

database_view_page()