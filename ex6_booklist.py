import os
import openai

openai.api_key_path = "/Users/shimonsant/PycharmProjects/gpt3/key.txt"

response = openai.Completion.create(
    model="text-davinci-003",
    # prompt="List 10 science fiction books:",
    prompt="List 10 bestsellers all time books:",
    temperature=0.5,
    max_tokens=200,
    top_p=1.0,
    frequency_penalty=0.52,
    presence_penalty=0.5,
    stop=["11."]
)
print(response.choices[0].text)
