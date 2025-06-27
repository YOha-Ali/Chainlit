import chainlit as cl
import google.generativeai as genai
# import os

# Set API key directly (or load from .env if using dotenv)
genai.configure(api_key="AIzaSyClKLOVc-o6awnksGP3S_f3VF1iu08oxtw") 

model = genai.GenerativeModel("gemini-2.0-flash")

@cl.on_message
async def main(message: cl.Message):
    response = model.generate_content(message.content)
    await cl.Message(content=response.text).send() 