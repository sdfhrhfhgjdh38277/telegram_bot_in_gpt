import g4f
import telebot as tele
from time import time

bot = tele.TeleBot("token")


@bot.message_handler(commands=["start"])
def start(message):
    # hello message, and update notification
    bot.reply_to(
        message,
        "Привет, я чат-бот основанный на ChatGPT 4. Ты можешь задать мне любой вопрос! Я отвечу на него."
        )

@bot.message_handler(content_types=["text"])
def ask_gpt(message):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4_32k,
        messages=[{"role": "user", "content": message}],
    )
    bot.send_message(message.chat.id, response)
    print(f"Request generated in: {time()}")


bot.infinity_polling()
