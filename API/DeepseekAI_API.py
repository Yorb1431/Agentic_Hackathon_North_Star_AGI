from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="",
)

completion = client.chat.completions.create(
    extra_headers={
        # Optional. Site URL for rankings on openrouter.ai.
        "HTTP-Referer": "<YOUR_SITE_URL>",
        # Optional. Site title for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>",
    },
    extra_body={},
    model="deepseek/deepseek-r1-zero:free",
    messages=[
        {
          "role": "user",
          "content": "What is the meaning of life?"
        }
    ]
)
print(completion.choices[0].message.content)
