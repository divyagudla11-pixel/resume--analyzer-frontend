import streamlit as st
import requests

st.title("Smart Resume Analyzer 🚀")

API_URL = "https://resume-analyzer-api.onrender.com/analyze"

file = st.file_uploader("Upload Resume PDF")

if file:
    files = {"file": file.getvalue()}
    
    response = requests.post(API_URL, files={"file": file})
    
    if response.status_code == 200:
        result = response.json()
        st.success("Analysis Done ✅")
        st.write("Category:", result["category"])
    else:
        st.error("Error connecting to API")