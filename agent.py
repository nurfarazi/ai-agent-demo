import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_ID = os.getenv("GOOGLE_MODEL_ID", "gemini-pro")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(MODEL_ID)
system_prompt = "You are an enthusiastic news reporter with a flair for storytelling!"

def get_response(user_input):
    convo = model.start_chat(history=[{"role": "user", "parts": [system_prompt]}])
    response = convo.send_message(user_input)
    return response.text

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print("Agent:", reply)
