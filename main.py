from config import get_settings
from fastapi import FastAPI, Request
import uvicorn
from fastapi.responses import JSONResponse


app = FastAPI()


@app.post('/')
async def read_root(request: Request):
    result = await request.json()
    print(result['message']['text'])
    return JSONResponse({'Hi': 'There'})


settings = get_settings()
if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8002, reload=True)


# import telebot

# bot = telebot.TeleBot(settings.tg_token)



# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id,
#                          "Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id,
#                          "Напиши привет")
#     else:
#         bot.send_message(message.from_user.id,
#                          "Я тебя не понимаю. Напиши /help.")
#     print(message.text)


# bot.polling(none_stop=True, interval=0)
