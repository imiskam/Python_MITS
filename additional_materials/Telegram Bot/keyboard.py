from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

# добавляем разметку наших кнопок
start = types.ReplyKeyboardMarkup(row_width=2)
# создаем кнопки информация
info = types.KeyboardButton('Информация')
# и статистика
stats = types.KeyboardButton('Статистика')
# и разработчик
creator = types.KeyboardButton('Разработчик')
# добавляем кнопки в нашу разметку
start.add(stats, info, creator)


"""------------------------------------------Добавление inline-кнопок-----------------------------------------------"""
"""
callback_data - строка, которую Telegram отправляет после нажатия кнопки пользователем. По ее содержимому Python-у 
удается понять, какая кнопка была нажата.
"""
stats = InlineKeyboardMarkup()  # разметка inline-кнопок
stats.add(InlineKeyboardButton('Да', callback_data='show_statistic'))  # создание кнопки "Да" c колбеком join
stats.add(InlineKeyboardButton('Нет', callback_data='cancel'))  # создание кнопки "Нет" с колбеком cancel
