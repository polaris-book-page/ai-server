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
user_category = "로맨스"
messages = [
    {"role": "system", "content": "You should help recommend books."},
    {"role": "system", "content": "You must answer in Korean."},
    {"role": "user", "content":  user_category + "책 4권 추천해줘. 이전에 추천한 책은 추천하지마. 최근 책으로 추천해줘"},
    {"role": "assistant", "content":  "책 이름만 써줘. 이전에 추천한 책은 추천하지마."},
]

# response
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.2,
)

# answer
answer = response.choices[0].message.content
print(answer)