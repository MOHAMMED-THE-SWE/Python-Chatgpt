# Importing openai module
from openai import OpenAI

client = OpenAI()
def creat_chatgpt(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content



if __name__ == "__main__":
    prompt = input("You: ")
    answer = creat_chatgpt(prompt)
    print(f"ChatGpt: {answer}")