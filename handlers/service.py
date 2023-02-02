from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import exceptions

from config.bot_config import bot
from config.mongo_config import users
from config.telegram_config import MY_TELEGRAM_ID


class GksManager(StatesGroup):
    waiting_station_name = State()
    waiting_station_confirm = State()


# обработка команды /reset - сброс клавиатуры и состояния
async def reset_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await state.reset_state()
    await message.answer(
        text='Сброс настроек бота выполнен, текущее действие отменено.',
        reply_markup=types.ReplyKeyboardRemove(),
    )
    await bot.delete_message(message.chat.id, message.message_id)


# обработка команды /users просмотр количества пользователей в БД
async def count_users(message: types.Message):
    queryset = list(users.find({}))
    users_count = len(queryset)
    final_text = ''
    for user in queryset:
        username = '{}, {}'.format(user['_id'], user['username'])
        final_text = '{}\n\n{}'.format(username, final_text)
    await message.answer(
        text=f'Количество пользователей в БД: {users_count}\n\n{final_text}'
    )


# обработка команды /log
async def send_logs(message: types.Message):
    file = f'logs_bot.log'
    with open(file, 'rb') as f:
        content = f.read()
        await bot.send_document(chat_id=MY_TELEGRAM_ID, document=content)


def register_handlers_service(dp: Dispatcher):
    dp.register_message_handler(reset_handler, commands='reset', state='*')
    dp.register_message_handler(count_users, commands='users')
