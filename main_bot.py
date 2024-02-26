#  import, token to bot
import g4f
import logging
import telebot as tele
from time import time
import configure as cfg

bot = tele.TeleBot(cfg.config["token"])


@bot.message_handler(commands=["start"])
def start(message):
    # hello message
    bot.send_message(
        message.chat.id,
        "Привет. Я твой карманный помощник на ближайшие запросы! Задай мне вопрос через команду /search (запрос),"
        "и я в течении минуты напишу тебе ответ!",
    )


@bot.message_handler(commands=["search"])
def ask_gpt(message):
    # send waiting message
    msg_wait = bot.send_message(
        message.chat.id, "Тааак, интересненько... дай-ка подумаю🤫"
    )
    msg_id = msg_wait.id
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
    bot.delete_message(message.chat.id, msg_id)
    bot.reply_to(message, response)
    print(f"Request generated in: {time()}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # start loogging bot
    # start polling to bot work
    bot.infinity_polling()
