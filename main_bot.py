# imports
import asyncio
import configure as cfg
import logging
import tracemalloc
import g4f
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

TOKEN_API = cfg.config["token"]  # Bot token
dp = Dispatcher()
tracemalloc.start()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет. Я твой карманный помощник на ближайшие запросы! Задай мне вопрос через команду /search (запрос), "
        "и я в течении минуты напишу тебе ответ!"
    )


async def main() -> None:
    bot = Bot(TOKEN_API)
    await dp.start_polling(bot)


@dp.message(Command("search"))
async def generation(message: Message):
    response = await g4f.ChatCompletion.create_async(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": message.text}],
    )
    await message.answer(response)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")
