from keyboard import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from create_bot import dp, bot 
from config import admin_id_list
from languages import *
from connect import check, write_update_lang, saveOneToJson

class FSMcreate(StatesGroup):
    faq_panel = State()
    change_lang_panel = State()

async def about_bot(message: types.Message):
	await FSMcreate.faq_panel.set()
	lang_code = await check(message.from_user.id)
	caption_text = await giveText(lang_code, '2')
	await bot.send_photo(chat_id=message.from_user.id, photo="https://i.imgur.com/1bz1Mp5.png", caption=caption_text, reply_markup=await giveButton(lang_code, '3'))

async def change_lang(message: types.Message, state: FSMContext):
    await FSMcreate.change_lang_panel.set()
    lang_code = await check(message.from_user.id)
    caption_text = (await giveText(lang_code, '3'))
    num = 1
    for i in arrOfLanguages:
        caption_text += f'\n<b>{num}</b> - {allNamesOfLangs[i]}'
        num +=1
    await bot.send_message(chat_id=message.from_user.id, text=caption_text, reply_markup=await giveButton(lang_code, '2'))

async def receiving_number_lang(message: types.Message, state: FSMContext):
    lang_code = await check(message.from_user.id)
    user_id = message.from_user.id
    try:
        new_lang_code = arrOfLanguages[int(message.text)-1]
        if new_lang_code != lang_code:
            lang_code = new_lang_code
            print(await write_update_lang(user_id, lang_code))
            print(await saveOneToJson(user_id, lang_code))
            await bot.send_message(chat_id=message.from_user.id, text=await giveText(lang_code,'5'), reply_markup=await giveButton(lang_code, '2'))
        else:
            await bot.send_message(chat_id=message.from_user.id, text=await giveText(lang_code,'4'))
    except:
        await bot.send_message(chat_id=message.from_user.id, text=await giveText(lang_code,'4'))

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
    dp.register_message_handler(back, text=back_buttons, state='*')
    dp.register_message_handler(about_bot, text=about_buttons, state=None)
    dp.register_message_handler(change_lang, text=change_lang_buttons, state=FSMcreate.faq_panel)
    dp.register_message_handler(receiving_number_lang, state=FSMcreate.change_lang_panel)
