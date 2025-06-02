import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import token
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message()
async def EchoBot(message: Message):
    text = message.text
    await message.answer(text)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
