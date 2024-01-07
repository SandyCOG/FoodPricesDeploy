import streamlit as st

# Set Page Configuration for a centered Layout
st.set_page_config(layout="centered")

# Configure page background color and font
st.markdown("""
<style> 
body {
    background-color: #007EA7;
    font-family: Arial, sans-serif;
}
</style>
""", unsafe_allow_html=True)

# Sidebar for menus
with st.sidebar:
    st.title("Menu")

