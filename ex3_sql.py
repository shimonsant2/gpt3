import os
import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key_path = "/Users/shimonsant/PycharmProjects/gpt3/key.txt"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Create a SQL request to find all users who live in California and have over 1000 credits:",
    temperature=0.3,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)
print(response.choices[0].text)
