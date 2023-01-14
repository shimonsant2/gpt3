import os
import openai

openai.api_key_path = "/Users/shimonsant/PycharmProjects/gpt3/key.txt"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a restaurant review based on these notes:\n\nName: The NONO\nPizza great, noisy, "
         "service polite, prices good.\n\nReview:",
  temperature=0.5,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
print(response.choices[0].text)