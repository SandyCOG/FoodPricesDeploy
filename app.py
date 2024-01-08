import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

# Set Page Configuration for a centered Layout
st.set_page_config(layout="wide")


# Configure page background color and font
st.markdown("""
<style> 
body {
    background-color: #007EA7;
    font-family: Arial, sans-serif;
}
</style>
""", unsafe_allow_html=True)

# Create a session state to manage page navigation
class SessionState:
    def __init__(self):
        self.page = "Introduction"  # Initial page

# Initialize session state
state = SessionState()

# Sidebar for page navigation
with st.sidebar:
    st.title("Navigation")
    pages = ["Introduction", "Authors", "Charts", "Prediction", "Feedback"]
    selected_page = st.radio("Go to:", pages, index=pages.index(state.page))
    go_button = st.button("Go")

# Handle page navigation
if go_button:
    state.page = selected_page

# Introduction Page
if state.page == "Introduction":
    st.title("Food Prediction Model")

    # Page content
    st.header("Introduction")
    st.write("Introduction content goes here.")

    st.header("Problem Statement")
    st.write("Problem statement goes here.")

    st.header("Objectives")
    st.write("Objectives go here.")

# Authors Page
elif state.page == "Authors":
    st.title("Food Prediction Model")

    # Page content
    st.header("Authors")
    st.write("Author information goes here.")

# Charts Page
elif state.page == "Charts":
    st.title("Food Prediction Model")

    # Page content
    st.header("Charts")
    # Generate example chart
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [10, 20, 15]})
    fig, ax = plt.subplots()
    ax.plot(df['x'], df['y'])
    st.pyplot(fig)

# Prediction Page
elif state.page == "Prediction":
    st.title("Food Prediction Model")

    # Page content
    st.header("Prediction")
    # Add your prediction model code here

# Feedback Page
elif state.page == "Feedback":
    st.title("Food Prediction Model")

    # Page content
    st.header("Feedback Form")

    # Feedback form
    name = st.text_input("Name:")
    email = st.text_input("Email:")
    feedback = st.text_area("Feedback:")
    submit_button = st.button("Submit Feedback")

    # Handle feedback submission
    if submit_button:
        # Save feedback to CSV file
        feedback_df = pd.DataFrame({'Name': [name], 'Email': [email], 'Feedback': [feedback]})
        feedback_df.to_csv('feedback.csv', mode='a', index=False, header=not pd.read_csv('feedback.csv').exists())

        st.success("Feedback submitted successfully!")

    st.header("Repository Link")
    st.write("Add your repository link here.")





