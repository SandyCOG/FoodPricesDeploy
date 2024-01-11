import streamlit as st   #imports streamlit library
import pandas as pd  #imports pandas library
import plotly.express as px #imports plotly
from streamlit.components.v1 import html 

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

# Update page in the session state
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
    st.title("Authors")

    # Sample author data
    authors_data = [
        {"name": "Author 1", "image": "url_to_image_1", "bio": "Bio of Author 1", "link": "https://linkedin.com/author1"},
        {"name": "Author 2", "image": "url_to_image_2", "bio": "Bio of Author 2", "link": "https://linkedin.com/author2"},
        # Add more authors as needed
    ]

    # Display authors in a 3 by 2 grid
    for i in range(0, len(authors_data), 2):
        col1, col2 = st.columns(2)
        
        # Column 1
        with col1:
            st.image(authors_data[i]["image"], width=150, caption=authors_data[i]["name"])
            st.write(authors_data[i]["bio"])
            st.markdown(f"[{authors_data[i]['name']}'s LinkedIn]({authors_data[i]['link']})")

        # Column 2
        with col2:
            # Check if there is a second author in the row
            if i + 1 < len(authors_data):
                st.image(authors_data[i + 1]["image"], width=150, caption=authors_data[i + 1]["name"])
                st.write(authors_data[i + 1]["bio"])
                st.markdown(f"[{authors_data[i + 1]['name']}'s LinkedIn]({authors_data[i + 1]['link']})")

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
