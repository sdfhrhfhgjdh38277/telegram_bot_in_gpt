#  import, token to bot
import g4f
import logging
import telebot as tele
from time import time
import configure as cfg

bot = tele.TeleBot(cfg.config["token"])
logging.basicConfig(filename="py_log.log", filemode="w")


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup()
    contact_btn = types.InlineKeyboardButton(text="Связаться с создателем", url="https://t.me/python_tor")
    markup.add(contact_btn)
    # hello message
    bot.send_message(message.chat.id, "Добро пожаловать! Если у вас возникнут вопросы или желание помочь - не стесняйтесь нажать на кнопку ниже для связи с разоаботчиком", reply_markup=markup)


@bot.message_handler(commands=["search"])
def ask_gpt(message):
    # send waiting message
    msg_wait = bot.send_message(
        message.chat.id, "Тааак, занимательно... сейчас нашаманю ответ🕊️"
    )
    msg_id = msg_wait.id
    # create generate model, and send generated message to user
    start_time = time()
    response = ChatCompletion.create(
        model=gemini_pro,
        messages=[{"role": "user", "content": message.text}],
    )
    bot.delete_message(message.chat.id, msg_id)
    bot_response = bot.reply_to(message, response)
    end_time = time()
    all_need_time = round(end_time - start_time, 2)
    print(f"Request generated in: {all_need_time}")
    
    
# Bot news
@bot.message_handler(commands=['news'])
def bot_new(message):
    bot.send_message(message.chat.id, 
    "Версия 0.5: Добавлена функция поиска ответов через википедию (отдельная команда, посмотреть можно в меню команд)")


if __name__ == "__main__":
   logging.basicConfig(level=logging.INFO)  # start loogging bot
    # start polling to bot work
    bot.infinity_polling()
