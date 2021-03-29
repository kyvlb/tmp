import logging

from keyboards.inline.callback_datas import choice_callback
from loader import bot, dp
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.choice_buttons import choice, red_keyboard, blue_keyboard
from loader import dp


@dp.message_handler(Command("poll"))
async def show_items(message: Message):
    await message.answer(text="Опрос: \n"
                            "Красная или синяя?",
                         reply_markup=choice)

@dp.callback_query_handler(text_contains="red")
async def chioce_red(call: CallbackQuery, number_of_people=1):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")

    await call.message.answer(f"Вы выбрали красный. Спасибо за ответ. Столько людей проголосовало за этот вариат: {number_of_people}",
                              reply_markup=red_keyboard)

@dp.callback_query_handler(choice_callback.filter(choice_name="blue"))
async def chioce_blue(call: CallbackQuery, callback_data: dict, number_of_people=3):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")

    await call.message.answer(f"Вы выбрали синюю. Спасибо за ответ. Столько людей проголосовало за этот вариат: {number_of_people}",
                              reply_markup=blue_keyboard)

