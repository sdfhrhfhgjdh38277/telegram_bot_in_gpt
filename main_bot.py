#  import, token to bot
import g4f
import telebot as tele
from time import time
import configure as cfg

bot = tele.TeleBot(cfg.config['token'])


@bot.message_handler(commands=["start"])
def start(message):
    # hello message
    bot.reply_to(
        message,
        "Привет, я чат-бот основанный на ChatGPT-4. Ты можешь задать мне любой вопрос! Я отвечу на него."
        "\nHо я могу не слишком точно давать ответы, поэтому прости если что-то будет не так!",
    )


@bot.message_handler(content_types=["text"])
def ask_gpt(message):
    # create generate model, and send generated message to user
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[
            {
                "role": "user",
                "content": message.text,
            }
        ],
    )
    bot.reply_to(message, response)
    print(f"Request generated in: {time()}")


bot.infinity_polling()
