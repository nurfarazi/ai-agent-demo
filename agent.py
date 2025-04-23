import agno
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  # Load from .env file

class OpenAIAgent(agno.Agent):
    def act(self, observation):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": observation}
            ]
        )
        return response.choices[0].message.content

if __name__ == "__main__":
    agent = OpenAIAgent()
    while True:
        user_input = input("You: ")
        reply = agent.act(user_input)
        print("Agent:", reply)
