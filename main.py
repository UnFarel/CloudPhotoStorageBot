import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import aiohttp


TOKEN = "5542040375:AAHpm4vEAHGnGW7Kj9bw5ACuxmqi4lDOVkY"
dp = Dispatcher()

logger = logging.getLogger(__name__)
class Userman:
    def __init__(self):
        self.photo_id = 0

@dp.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, <b>{message.from_user.full_name}</b>, загрузи фото)")


@dp.message(content_types="text")
async def download_photo(message: types.Message, bot: Bot):
    await bot.download(
        message.photo[-1],
        destination=f"/photo_storage/{message.photo[-1].file_id}.jpg"
    )


def main() -> None:
    bot = Bot(TOKEN, parse_mode="HTML")
    dp.run_polling(bot)


if __name__ == "__main__":
    main()