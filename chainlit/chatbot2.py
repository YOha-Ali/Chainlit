import chainlit as cl
import google.generativeai as genai
from datetime import datetime
import pytz

# Gemini model setup
genai.configure(api_key="AIzaSyClKLOVc-o6awnksGP3S_f3VF1iu08oxtw")
model = genai.GenerativeModel("gemini-2.0-flash")

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content.lower()

    if "time" in user_input or "date" in user_input:
        pk_time = datetime.now(pytz.timezone("Asia/Karachi")).strftime("%Y-%m-%d %H:%M:%S")
        reply = f"Aaj Pakistan mein waqt hai: {pk_time}"
    else:
        response = model.generate_content(user_input)
        reply = response.text

    await cl.Message(content=reply).send()


# import requests

# def get_weather(city="Lahore"):
#     api_key = ""
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     data = response.json()

#     if data.get("main"):
#         temp = data["main"]["temp"]
#         desc = data["weather"][0]["description"]
#         return f"The weather in {city} is {desc} with {temp}°C."
#     else:
#         return "Sorry, weather data not found."

