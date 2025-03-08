def test_deepseek_ai(email):

    import requests
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer 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",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek/deepseek-r1-zero:free",
            "messages": [
                {
                    "role": "user",
                    "content": email
                }
            ]
        }
    )
    data = response.json()
    if data["choices"][0]["message"]["content"].find("phishing") != -1:
        return "phishing"
    return "no phishing"
