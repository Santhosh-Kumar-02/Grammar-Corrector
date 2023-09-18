import streamlit as st
import requests
from PIL import Image
import time

API_URL = "https://api-inference.huggingface.co/models/grammarly/coedit-large"
headers = {"Authorization": st.secrets["auth_token"]}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def clear_input():
    st.session_state["input_text"] = ""

def break_line():
    html_str = f"""
    <br>
    """
    st.markdown(html_str, unsafe_allow_html=True)
	
st.markdown(
    """
    <style>
    .css-q8sbsg p {
        font-size: 20px;
		font-weight: 600;
    }
    </style>""",unsafe_allow_html=True)

image = Image.open('CoEdit.png')
st.image(image)
break_line()

instructions = {
	"Fix the grammar": "Please review the following paragraph and correct any grammatical errors you find. Make sure the sentences are clear and well-structured: ", 
	"Paraphrase": "Please paraphrase the following paragraph while maintaining its original meaning: ",
	"Summarize": "Please provide a concise summary of the main points and key ideas presented in the following paragraph:"}

option = st.selectbox('Select Instruction:', options= list(instructions.keys()))
input_text = st.text_area("Input:", key='input_text')

col1, col2 = st.columns([2,15])
with col1:
	submit_button = st.button("Submit", type="primary")
with col2:
	clear_all_btn= st.button(label="Clear All", on_click=clear_input, type="secondary")

break_line()
if input_text or submit_button:
	with st.spinner('Processing...'):
		time.sleep(2)
		data = query({"inputs": instructions[option]+ f"\"{input_text}\""})

		st.markdown("""<p style="font-weight: 600; font-size: 20px;">Output</p>""", unsafe_allow_html=True)
		st.markdown(f"""<div style="text-align: justify; color: black; font-weight: 550; line-height: 1.35; padding: 18px; border-radius: 0.5rem; background-color: #FFFFFF;">
		{data[0]["generated_text"]}</div>""", unsafe_allow_html=True)
