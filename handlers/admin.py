from create_bot import bot, dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from keyboard import *
from config import admin_id_list
from connect import check, write_update_lang

arrPasses = ["/adminDFhj32h45h4187ipoO09FD78fghjg"]

class FSMcreate(StatesGroup):
    admin_panel = State()

async def admin_start(message: types.Message):
	await FSMcreate.admin_panel.set()
	await bot.send_message(message.from_user.id, 'You are in admin panel', reply_markup=admin_key)

async def main_menu(message: types.Message, state: FSMContext):
	await bot.send_message(message.from_user.id, 'IAMHACKER')


async def back(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    lang_code = await check(message.from_user.id)
    main_key = await giveButton(lang_code, '1')
    await bot.send_message(chat_id = message.from_user.id, text = 'Ok', reply_markup=main_key)

def register_handlers_create(dp: Dispatcher):
    dp.register_message_handler(back, state='*', commands=['Назад'])
    dp.register_message_handler(back, Text(equals='назад', ignore_case=True), state='*')
    dp.register_message_handler(admin_start, text=arrPasses, state = None)
    dp.register_message_handler(main_menu, text='IAMHACKER', state = FSMcreate.admin_panel)