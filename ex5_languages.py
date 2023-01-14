import os
import openai

openai.api_key_path = "/Users/shimonsant/PycharmProjects/gpt3/key.txt"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Translate this into 1. French, 2. Spanish and 3. Japanese and 4. Hebrew :\n\nWhat rooms do you have "
         "available?\n\n1.",
  temperature=0.3,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
print(response.choices[0].text)