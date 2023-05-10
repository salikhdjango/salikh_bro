from django.shortcuts import render
import requests


# Create your views here.
def main_view(request):
    return render(request, 'index.html', {'1': '1'})


def send_telegram(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')

        message = f'Ism : {name}\nEmail : {email}\nDescription : {desc}'

        send_to_telegram(message)
        return render(request, 'success.html')
    return render(request, 'form.html')


def send_to_telegram(message):
    bot_token = '5747389813:AAHyCKcY-Q-wdaWbIC-3CmuYpDUTaWBB2U0'
    chat_id = '1732668204'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, json=payload)
    if response.ok:
        print('Xabar yuborildi')
    else:
        print('Xatolik yuz berdi:', response.text)
