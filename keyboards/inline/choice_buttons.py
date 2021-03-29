from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.config import URL_RED, URL_BLUE
from keyboards.inline.callback_datas import choice_callback

# choice = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Красная", callback_data=choice_callback.new(choice_name="red", number_of_people=3)),
#             InlineKeyboardButton(text="Синяя", callback_data=choice_callback.new(choice_name="blue", number_of_people=0)),
#         ],
#         [
#             InlineKeyboardButton(text="Получить результаты опроса", callback_data="cancel")
#         ]
#     ]
# )

choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="Красная", callback_data=choice_callback.new(choice_name="red", number_of_people=1))
choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="Синяя", callback_data="choice:red:3")
choice.insert(buy_apples)

cancel_button = InlineKeyboardButton(text="Получить результаты опроса", callback_data="cancel")
choice.insert(cancel_button)

red_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Добро пожаловать. Жми, чтобы перейти", url=URL_RED)
        ]
    ]
)

blue_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Хороший выбор. Жми, чтобы перейти", url=URL_BLUE)
        ]
    ]
)