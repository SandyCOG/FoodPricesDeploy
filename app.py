import streamlit as st #imports streamlit library

# Set Page Configuration for a centered Layout
st.set_page_config(layout="centered")

#configure page background colour and font
st.markdown("""
<style> 
body {
            background-color: #007EA7;
            font-family: Arial, sans-serif;
""")

# Sidebar for menus
with st.sidebar:
st.title("Menu")
