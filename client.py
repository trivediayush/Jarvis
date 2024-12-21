from openai import OpenAI
import os
client = OpenAI(
    api_key="",# use your own api key
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system", "content":"You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "What is coding"}
    ]
)

print(completion.choices[0].message.content)