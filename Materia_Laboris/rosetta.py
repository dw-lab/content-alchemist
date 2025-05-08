import requests


def chat_with_model(token):
    url = 'https://llm-hub.dw.com/openai/api/chat/completions'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
        "model": "anthropic.claude-3-5-sonnet-20240620-v1:0",
        "messages": [
            {
                "role": "user",
                "content": "Why is the sky blue?"
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


token = "sk-e40d0b00489d46738988d269e5b07b9e"
response = chat_with_model(token)
print(response)
