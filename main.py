import os
from openai import OpenAI


api_key = os.environ.get('OPENAI_API_KEY',"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")

print(api_key)

client = OpenAI(
    api_key=api_key
)

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(api_key)
    print("Hello world!")
