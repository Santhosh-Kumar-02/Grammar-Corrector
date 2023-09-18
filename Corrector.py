import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/grammarly/coedit-large"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

st.title("Grammar Corrector")

text = st.text_input("Enter text:")
text = "Please correct the following sentence:" + text
button = st.button("Correct grammar")

if button:
	data = query({"inputs": text})
	st.write(data[0]["generated_text"])
