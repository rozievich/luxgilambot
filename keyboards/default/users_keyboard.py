from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db

users_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Бизнинг Каталог 📒")

        ],
        [
            KeyboardButton("Боғланиш ☎️")
        ],
        [
            KeyboardButton("Ижтимоий тармоқларимиз 📱")
        ]
    ], resize_keyboard=True
)


send_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📱 Контактимни улашиш 📱', request_contact=True),
        ]
    ], resize_keyboard=True
)
