import streamlit as st
import requests
from PIL import Image

# Custom CSS for modern styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .stSidebar {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stTextInput input {
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
        border: 1px solid #ddd;
    }
    .stMarkdown h1 {
        color: #2c3e50;
    }
    .stMarkdown h2 {
        color: #34495e;
    }
    .stMarkdown p {
        color: #7f8c8d;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title and Description
st.title("Titanic Dataset Chatbot 🚢")
st.markdown(
    """
    Welcome to the **Titanic Dataset Chatbot**! Ask me anything about the Titanic dataset, and I'll provide you with insights and visualizations.
    """
)

# Sidebar for additional information
st.sidebar.header("About")
st.sidebar.markdown(
    """
    This chatbot is designed to answer questions about the Titanic dataset, including:
    - Passenger demographics
    - Survival rates
    - Fare and class distributions
    - And much more!
    """
)

# Input for user question
question = st.text_input("Enter your question about the Titanic dataset:", placeholder="e.g., What percentage of passengers were male?")

# Submit button
if st.button("Submit"):
    if question:
        # Send the question to the backend
        response = requests.post("http://localhost:8000/analyze", json={"question": question}).json()
        
        # Display the response
        if "response" in response:
            if response["response"].endswith(".png"):
                # If the response is an image, display it
                image = Image.open(response["response"])
                st.image(image, caption="Visualization", use_column_width=True)
            else:
                # If the response is text, display it in a styled box
                st.markdown(
                    f"""
                    <div style="
                        background-color: #ffffff;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                        margin-top: 20px;
                    ">
                        <h3>Response:</h3>
                        <p>{response["response"]}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.error("Failed to get a response from the server.")
    else:
        st.warning("Please enter a question.")

# Footer
st.markdown(
    """
    ---
    **Note:** This chatbot is powered by Streamlit and a custom backend. For more information, visit the [GitHub repository](#).
    """
)