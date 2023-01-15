import openai

openai.api_key_path = "/Users/shimonsant/PycharmProjects/gpt3/key.txt"

response = openai.Completion.create(
    model="text-davinci-003",
    # prompt="Create a list of 8 questions for my interview with a science fiction author:",
    # prompt="Create a list of 10 questions for my interview with a teacher:",
    # prompt="Create a list of 18 questions for my interview in aws annapurna as an automation software engineer:",
    # prompt="Create a list of 18 questions for my interview in product management",
    prompt="Create a list of 20 questions for my interview in amazon as testing software engineer",
    # prompt="Create a list of 20 latest trends in software testing",
    temperature=0.5,
    max_tokens=300,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)
print(response.choices[0].text)
