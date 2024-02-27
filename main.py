import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPEN_API_KEY"),
)

# model
model = "gpt-3.5-turbo"

# query, message
messages = [
    {"role": "system", "content": "You should help recommend books."},
    {"role": "system", "content": "You must answer in Korean."},
    {"role": "user", "content": "SF소설 책 추천해줘."}
]

# response
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.3,
)

# answer
answer = response.choices[0].message.content
print(answer)