import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

# подключение модуля с токеном
import config
# подключение модуля с кнопками
import keyboard

"""-------------------------------------- настройка бота и логирование -------------------------------------------"""

# хранилище состояний
storage = MemoryStorage()
# инициализация бота
bot = Bot(config.TOKEN, parse_mode=types.ParseMode.HTML)
# инициализация диспетчера, при этом указываем ему на хранилище состояний
dp = Dispatcher(bot, storage=storage)
# подключаем логирование
logging.basicConfig(
    # указываем название с логами
    filename='log.txt',
    # указываем уровень логирования
    level=logging.INFO,
    # указываем формат сохранения логов
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s '
           u'[%(asctime)s] %(message)s')
"""---------------------------------------------- настройка FMS -----------------------------------------------------"""


class Me_info(StatesGroup):
    Q1 = State()  # задаем состояние 1
    Q2 = State()  # задаем состояние 2


# прописываем хендлер на команду me, при этом изначальное состояние не задаем
@dp.message_handler(Command('me'), state=None)  # создаем команду /me для админа
async def enter_me_info(message: types.Message):
    # сверяем id с id администратора
    if message.chat.id == config.ADMIN_ID:
        # бот отправит сообщение
        await message.answer("Начинаем настройку \n"
                             "1. Укажите ссылку на Ваш профиль")
        # после чего мы изменяем состояние Q1
        await Me_info.Q1.set()  # начинает ждать наш ответ, задав состояние Q1


# задаем хендлер для состояния Q1
# обратите внимание, что к состоянию мы обращаемся через атрибут класса
@dp.message_handler(state=Me_info.Q1)
# нашей функции мы указываем, что хотим получить сообщение и состояние
async def answer_for_state_Q1(message: types.Message, state: FSMContext):
    # сохраняем текст полученного сообщения
    answer = message.text
    # в данном месте прописываем для нашего состояния обновление данных
    # в пространство имен для текущего состояния
    # мы добавляем ключ answer1 со значением answer, далее мы в этом убедимся
    await state.update_data(answer1=answer)
    # после чего выводим сообщение
    await message.answer("Ваша ссылка сохранена \n"
                         "2. Введите текст")
    # и задаем состояние Q2
    await Me_info.Q2.set()


# задаем хендлер для обработки данных от пользователей, находящихся во втором состоянии
# т.е. бот будет отлавливать пользователей, которые перейдут в состояние Q2
@dp.message_handler(state=Me_info.Q2)
async def answer_for_state_Q2(message: types.Message, state: FSMContext):
    # записываем ответ
    answer = message.text
    # Снова в пространство имен добавляем answer2 со значением answer, т.е. с текстом пользователя
    await state.update_data(answer2=answer)
    # говорим боту отправить сообщение
    await message.answer("Текст сохранен")
    # в переменную data получаем словарь, хранящийся в нашем хранилище состояний для текущего состояния
    data = await state.get_data()
    # print(data)
    # достаем значение по ключу answer1
    answer1 = data.get("answer1")
    # достаем значение по ключу answer2
    answer2 = data.get("answer2")
    # открываем файл link.txt на режим записи в кодировке UTF-8
    with open("link.txt", 'w', encoding="UTF-8") as link_txt:
        # записываем строкой ссылку в наш файл
        link_txt.write(str(answer1))
    # открываем файл text.txt в режиме записи в той же кодировке
    with open("text.txt", "w", encoding="UTF-8") as text_txt:
        # записываем в файл текст, который передал пользователь
        text_txt.write(str(answer2))
    # говорим боту отправить сообщение
    await message.answer(f"Ваша ссылка на профиль: {answer1} \n"
                         f"Ваш текст: {answer2}")
    # закрываем текущее состояние
    await state.finish()


""" -------------------------------------- обработка команды /start ----------------------------------------------"""


# подключаем handler на команду start, указываем состояние равное None
@dp.message_handler(commands='start', state=None)
async def welcome(message: types.Message):
    # открываем файл user.txt в режиме чтения
    joined_file = open('user.txt', 'r')
    # создаем множество для хранения имен всех пользователей
    joined_users = set()
    # проходим циклом по каждому пользователю в user.txt
    for line in joined_file:
        # добавляем их в наше множество пользователей
        joined_users.add(line.strip())
    # если пользователь, который нажал /start
    # находится во множестве пользователей
    if not str(message.chat.id) in joined_users:
        # открываем файл user.txt на дозапись
        joined_file = open('user.txt', 'a')
        # записываем в него id нашего пользователя
        joined_file.write(str(message.chat.id) + '\n')
        # добавляем его во множество пользователей
        joined_users.add(message.chat.id)
        # говорим боту отправить сообщение, при этом
    await bot.send_message(
        # обращаемся к id пользователя
        message.chat.id,
        # указываем отправляемое сообщение hello + имя пользователя
        f'Hello {message.from_user.first_name}',
        # подключаем кнопки из файла keyboard, обратившись к переменной start
        reply_markup=keyboard.start)


"""
-------------------------------------->>>> БЛОК КОДА ДЛЯ РАБОТЫ С РАССЫЛКОЙ<<<< ----------------------------------------
В данной части рассмотрен хендлер для рассылки пользователем бота и отправка им фотографий.
"""


# создаем обработчик сообщений для mailing_list
@dp.message_handler(commands=['mailing_list'])
# задаем функцию обработчик
async def mailing_list(message : types.Message):
    # сверяем id пославшего сообщение с id админа
    if message.chat.id == config.ADMIN_ID:
        # отправляем сообщение
        await bot.send_message(message.chat.id, f'*Рассылка началась'
                                                f'\nБот оповестит, когда закончит рассылку*',
                               parse_mode=types.ParseMode.MARKDOWN_V2)
        # задаем переменные для хранения принявших и заблокировавших
        recieve_users, block_users = 0, 0
        # открываем user.txt в режиме чтения
        with open('user.txt', 'r') as file:
            # создаем множество всех пользователей
            joined_users = set()
            # проходим циклу по всем id в файле
            for line in file:
                # добавляем во множество id
                joined_users.add(line.strip())
            # запускаем цикл
            for user in joined_users:
                try:
                    await bot.send_photo(user, open('python.png', 'rb'))
                    recieve_users += 1
                except:
                    block_users += 1
                await asyncio.sleep(0.4)
            await bot.send_message(message.chat.id, f'Рассылка завершена \n'
                                                    f'Сообщение получили: *{recieve_users}* пользователей \n'
                                                    f'Заблокировали бота: *{block_users}*',
                                   parse_mode=types.ParseMode.MARKDOWN_V2)


"""

-------------------------------------->>>> БЛОК КОДА С ИНФОРМАЦИЕЙ И СТАТИСТИКОЙ<<<< -----------------------------------
Данная часть кода для работы с получением информации о пользователях.
Здесь расположены хендлеры для обработки команд Информация и Статистка.
Также в этом блоке содержаться хендлеры для работы с выводом информации о количестве посетителей
"""

""" _______________________________________кнопка /Информация и /Статистика__________________________________________"""


# задаем обработчик для нашей кнопки, указываем тип контента как text
@dp.message_handler(content_types=['text'])
# задаем функцию-обработчик
async def info_static(message: types.Message):
    # если переданное боту сообщение = 'Информация'
    if message.text == 'Информация':
        # бот отправляет сообщение пользователю, отправившего его
        print(message.chat.id)
        await bot.send_message(message.chat.id,
                               # с текстом
                               text='Бот \nсоздан в образовательных целях',
                               # режим форматирования
                               parse_mode='Markdown')
    elif message.text == 'Статистика':
        await bot.send_message(
            message.chat.id,
            text='Хочешь посмотреть статистику бота?',
            reply_markup=keyboard.stats)

    elif message.text == "Разработчик":
        # открываем наш файл link.txt
        with open("link.txt", encoding="UTF-8") as link_txt:
            # считываем его содержимое в переменную link
            link = link_txt.read()
        with open("text.txt", encoding="UTF-8") as text_txt:
            text = text_txt.read()
        await bot.send_message(message.chat.id, text=f"Разработчик: {link} \n {text}")


"""_______________________________________ обработка inline-кнопки "Да"______________________________________________"""


# подключаем обработчик входящих запросов
# при этом входящий запрос должен содержать строку show_statistic (text_contains='show_statistic')
@dp.callback_query_handler(text_contains='show_statistic')
# создаем функцию-обработчик
# при этом функция show_statistic будет ожидать аргумент call с типом обратного запроса
async def show_statistic(call: types.CallbackQuery):
    # если id пользователя, пославшего запрос, соответствует id администратора
    if call.message.chat.id == config.ADMIN_ID:
        # считаем количество всех пользователей
        d = sum(1 for line in open('user.txt'))
        # говорим боту изменить сообщение
        await bot.edit_message_text(
            # чатом будет являться id чата, из которого пришло сообщение
            chat_id=call.message.chat.id,
            # id сообщения, которое нужно изменить, будет сообщением, по id сообщения в поступившем запросе
            message_id=call.message.message_id,
            # выводим необходимую информацию
            text=f'Статистка посетителей: {d} посетителей')
    else:
        # если же id запросившего не совпадет с id администратора
        await bot.edit_message_text(
            # прописываем тот же путь до сообщения
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            # и выводим следующий текст
            text='У Вас отсутствуют права администратора')


"""_______________________________________ обработка inline-кнопки "Нет" ____________________________________________"""


# задаем хендлер для команды cancel
# при этом входящий запрос должен содержать строку cancel
@dp.callback_query_handler(text_contains='cancel')
async def cancel(call: types.CallbackQuery):
    # говорим боту изменить сообщение
    # прописав путь до этого сообщения
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text="Вы вернулись в главное меню")


""" -------------------------------------- точка входа --------------------------------------------------------"""
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
