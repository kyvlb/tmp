from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config

from loader import dp, bot
from utils.notify_admins import on_startup_notify

async def on_startup(dispatcher):
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

async def on_shutdown(dp):
    await bot.close()

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup)