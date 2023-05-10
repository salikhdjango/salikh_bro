from django.urls import path
from .views import main_view, send_telegram

app_name = 'pages'

urlpatterns = [
    path('', main_view, name='mainview'),
    path('send-telegram/', send_telegram, name='send-telegram'),
]