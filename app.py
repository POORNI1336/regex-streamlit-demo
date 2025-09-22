import re
import streamlit as st

st.title("Regex Demo in Streamlit")

text = st.text_area("Enter text here:")
pattern = st.text_input("Enter regex pattern:")

if st.button("Run Regex"):
    try:
        matches = re.findall(pattern, text)
        st.write("Matches found:", matches)
    except re.error as e:
        st.error(f"Invalid regex: {e}")
