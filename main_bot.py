import g4f
import telebot as tele
from time import time

bot = tele.TeleBot("6719622488:AAEvOetK4PPPJs8a8LMqZAke5isOHFLMzpg")


@bot.message_handler(commands=["start"])
def start(message):
    # hello message, and update notification
    bot.reply_to(
        message,
        "Привет, я чат-бот основанный на ChatGPT 3.5. Ты можешь задать мне любой вопрос! Я отвечу на него."
        "Но я могу не слишком точно давать ответы, поэтому прости если что-то будет не так!\nОт разработчика - напиши "
        "язык на котором хочешь сделать вывод(Иначе выведется на английском)",
    )
    bot.send_message(
        message.chat.id,
        "Обновление 0.2 - Изменена система поиска: вместо обычных сообщений теперь выступает команда /search ("
        "запрос). В дальнейшем планируется добавить поддержку групп",
    )


@bot.message_handler(commands=["search"])
def ask_gpt(message):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4_32k,
        messages=[
            {"role": "user", "content": message.ask_gpt},
            {
                "role": "assistant",
                "content": ...,
            },  # there must be contained last bot message, but i don`t make this in soon.
        ],
    )
    bot.send_message(message.chat.id, response)
    print(f"Request generated in: {time()}")


bot.infinity_polling()
