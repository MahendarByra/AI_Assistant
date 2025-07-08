from openai import OpenAI
import os

def get_ai_reply(user_text):
    """
    Get AI response for the input text using GPT-3.5 Turbo.
    """
    # Initialize client with your API key
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant named Jarvis."},
            {"role": "user", "content": user_text}
        ],
        temperature=0.6
    )

    reply = completion.choices[0].message.content.strip()
    return reply

