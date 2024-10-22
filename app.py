import openai

# openai.api_key = "org-jvs4QRXp6sRVSRbv61aiVSNa"

# def generate_image(prompt):
#   response = openai.Image.create(
#       prompt=prompt,
#       n=1,
#       size="1024x1024"
#   )
#   image_url = response.data[0].url
#   return image_url

# prompt = input("Enter your text prompt: ")
# image_url = generate_image(prompt)
# print(image_url)

import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# .env फाइल से API की कुंजी लोड करें
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
  client = OpenAI()
  response = client.images.generate(
      model="image-alpha-001",
      prompt=prompt,
      n=1,
      size="1024x1024"
  )
  image_url = response.data[0].url
  return image_url

# Streamlit यूजर इंटरफेस बनाएं
st.title("Text-to-Image Generator")
prompt = st.text_input("Enter your prompt:")

if st.button("Generate Image"):
  if prompt:
    image_url = generate_image(prompt)
    st.image(image_url)
  else:
    st.warning("Please enter a prompt.")