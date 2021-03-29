from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Для начала диалога",
            "/help - Список команд",
            "/poll - Создать голосование",
            )

    await message.answer("\n".join(text))
