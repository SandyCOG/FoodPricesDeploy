import streamlit as st   #imports streamlit library
import pandas as pd  #imports pandas library
import matplotlib.plt as plt #imports matplotlib

#set page configuration for centered layout
st.set_page_config(layout="wide", page_title="Your Page Title", page_icon="🌐", theme="wide")

# Configure page background color and font
st.markdown(
    """
    <style> 
        body {
            background-color: #007EA7;
            font-family: Arial, sans-serif;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Create a session state to manage page navigation
class SessionState:
    def __init__(self):
        self.page = "Introduction"  # Initial page

# Initialize session state
state = SessionState()

# Sidebar for page navigation
st.sidebar.title("Navigation")
pages = ["Introduction", "Authors", "Charts", "Prediction", "Feedback"]
selected_page = st.sidebar.radio("Go to:", pages, index=pages.index(state.page))
