from openai import OpenAI
client = OpenAI(api_key = "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")

response = client.chat.completions.create(
    model="o1-preview",
    messages=[
        {
            "role": "user", 
            "content": "Write a bash script that takes a matrix represented as a string with format '[1,2],[3,4],[5,6]' and prints the transpose in the same format."
        }
    ]
)

print(response.choices[0].message.content)
