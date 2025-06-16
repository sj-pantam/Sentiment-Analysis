import streamlit as st
import requests

st.title("Sentiment Analyzer (Mistral)")

text_input = st.text_area("Enter your sentence here:")

if st.button("Analyze"):
    response = requests.post("http://localhost:8003/analyze", data={"text": text_input})
    sentiment = response.json().get("sentiment", "Error getting sentiment")
    st.subheader('Predicted Sentiment')
    st.write(sentiment)