import g4f
import telebot as tele
import token
bot = tele.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "Привет, я чат-бот основанный на ChatGPT 3.5. Ты можешь задать мне любой вопрос! Я отвечу на него."
        "Но я могу не слишком точно давать ответы, поэтому прости если что-то будет не так!\nОт разработчика - напиши язык на котором хочешь сделать вывод(Иначе выведется на английском)",
    )


@bot.message_handler(content_types=["text"])
def text(message):
    response = (
        (
            g4f.ChatCompletion.create(
                model=g4f.models.gpt_35_turbo,
                messages=[{"role": "user", "content": message}],
            ),
        ),
    )
    bot.send_message(message.chat.id, response)


bot.infinity_polling()
