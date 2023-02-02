import logging

from aiogram import types
from aiogram.utils import executor

from config.bot_config import bot, dp
# from config.telegram_config import MY_TELEGRAM_ID
from handlers.service import register_handlers_service

logging.basicConfig(
    filename='logs_bot.log',
    level=logging.INFO,
    filemode='a',
    format='%(asctime)s - %(message)s',
    datefmt='%d.%m.%y %H:%M:%S',
    encoding='utf-8',
)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(text='Привет')


# @dp.message_handler(commands=['help'])
# async def help_handler(message: types.Message):
#     await bot.send_message(
#         message.chat.id,
#         text=f'{HELP_TEXT}'
#     )


# обработка события - добавление бота в группу
@dp.message_handler(content_types=['new_chat_members'])
async def add_bot_message(message: types.Message):
    # удаление сервисного сообщения 'добавлен пользователь'
    try:
        await bot.delete_message(message.chat.id, message.message_id)
    except:
        pass


# удаление сервисного сообщения 'пользователь удалён'
@dp.message_handler(content_types=['pinned_message', 'left_chat_member'])
async def delete_service_pinned_message(message: types.Message):
    try:
        await bot.delete_message(message.chat.id, message.message_id)
    except:
        pass


# async def on_startup(_):
#     scheduler_jobs()


if __name__ == '__main__':
    # scheduler.start()
    register_handlers_service(dp)
    executor.start_polling(dp, skip_updates=True)
    # executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
