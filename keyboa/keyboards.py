from aiogram import types

button1=types.KeyboardButton(text='/start')
button2=types.KeyboardButton(text='/stop')
button3=types.KeyboardButton(text='Инфо')
button4=types.KeyboardButton(text='Найти лису')
button5=types.KeyboardButton(text='/prof')
button6=types.KeyboardButton(text='Показать лису')
button7=types.KeyboardButton(text='/lifts')

keyboard1=[
    [button1, button2],
    [button4, button5, button7],
]
keyboard2=[
    [button3, button6],
]

kb1=types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2=types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)

