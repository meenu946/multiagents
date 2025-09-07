import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/solve-doubt"

st.set_page_config(page_title="EduNinja AI Agents", page_icon="🧠")

st.title("🧠 EduNinja AI Agents")
st.markdown("Use this tool to get explanations, debug suggestions, quizzes, and motivation for coding doubts.")

# Input Fields
doubt = st.text_area("❓ Enter your doubt:")
code = st.text_area("💻 Enter your code (optional):")

if st.button("Solve Doubt"):
    if not doubt.strip():
        st.warning("Please enter your doubt!")
    else:
        payload = {
            "doubt": doubt,
            "code": code
        }
        with st.spinner("Processing your request..."):
            try:
                response = requests.post(API_URL, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    st.subheader("📘 Explanation")
                    st.write(data.get("explanation", "No explanation available."))

                    st.subheader("🐞 Debug Suggestions")
                    st.write(data.get("debug", "No debug suggestions available."))

                    st.subheader("📝 Quiz Questions")
                    st.write(data.get("quiz", "No quiz available."))

                    st.subheader("🎯 Motivation")
                    st.write(data.get("motivation", "Stay motivated!"))
                else:
                    st.error(f"Error: {response.status_code}")
            except requests.exceptions.RequestException as e:
                st.error(f"Request failed: {str(e)}")
