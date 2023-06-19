from fastapi import requests
from config import get_settings


settings = get_settings()
whook = 'https://b98e-5-44-169-109.eu.ngrok.io'  # redirect from localhost to ngrok service

rget = requests.get(f'https://api.telegram.org/bot{settings.tg_token}/deleteWebhook')
print(rget.json())

rget = requests.get(f'https://api.telegram.org/bot{settings.tg_token}/setWebhook?url=https://{whook}/&allowed_updates[]=message')

print(rget.json())
