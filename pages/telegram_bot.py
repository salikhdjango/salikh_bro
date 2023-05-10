import requests



def send_to_telegram(message):
    bot_token = ""
    chat_id = "1732668204"
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, json=payload)
    return response.ok
