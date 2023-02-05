from keyboard import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from create_bot import dp, bot 
from config import admin_id_list, openai_api_key
from languages import *
from connect import check, write_update_lang, saveOneToJson
# import openai
from gpt3api import make_openai_request

# openai.api_key = openai_api_key

class FSMcreate(StatesGroup):
    first_part = State()

async def about_bot(message: types.Message):
	await FSMcreate.first_part.set()
	lang_code = await check(message.from_user.id)
	await bot.send_message(chat_id = message.from_user.id, text = await giveText(lang_code, '6'), reply_markup=await giveButton(lang_code, '2'))

async def find_answer(message: types.Message, state: FSMContext):
	lang_code = await check(message.from_user.id)
	user_text = str(message.text)


	prompt_y_n = f'''"{user_text}" is this connected to cooking or receipts, say only "Yes" or "No"?'''
	response = await make_openai_request(prompt_y_n)
	reply = str(response['choices'][0]['text'])
	if 'Yes' in reply:
		response = await make_openai_request(user_text)
		answer = response['choices'][0]['text']
		await bot.send_message(chat_id = message.from_user.id, text = answer, reply_markup=await giveButton(lang_code, '2'))
	else:
		await bot.send_message(chat_id = message.from_user.id, text = await giveText(lang_code, '4'), reply_markup=await giveButton(lang_code, '2'))
	
	text_for_admin = f'{message.from_user}\n\nasked:{user_text}'
	for i in admin_id_list:
		await bot.send_message(chat_id=i, text=text_for_admin)



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
    dp.register_message_handler(about_bot, text=rec_tips_buttons, state='*')
    dp.register_message_handler(find_answer, state=FSMcreate.first_part)








# from keyboard import *
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.dispatcher.filters import Text
# from aiogram import types, Dispatcher
# from create_bot import dp, bot 
# from config import admin_id_list, openai_api_key
# from languages import *
# from connect import check, write_update_lang, saveOneToJson
# import openai

# openai.api_key = openai_api_key

# class FSMcreate(StatesGroup):
#     first_part = State()

# async def about_bot(message: types.Message):
# 	await FSMcreate.first_part.set()
# 	lang_code = await check(message.from_user.id)
# 	await bot.send_message(chat_id = message.from_user.id, text = await giveText(lang_code, '6'), reply_markup=await giveButton(lang_code, '2'))

# async def find_answer(message: types.Message, state: FSMContext):
# 	lang_code = await check(message.from_user.id)
# 	response = openai.Completion.create(
# 		engine="text-davinci-003",
# 		prompt=f'''{message.text}" is this connected to cooking or receipts, say only "Yes" or "No"?''',
# 		max_tokens=1024,
# 		n=1,
# 		stop=None,
# 		temperature=0.5,
# 	)
# 	reply = str(response.choices[0].text)
# 	if 'Yes' in reply:
# 		response = openai.Completion.create(
# 			engine="text-davinci-003",
# 			prompt=message.text,
# 			max_tokens=1024,
# 			n=1,
# 			stop=None,
# 			temperature=0.5,
# 		)
# 		answer = response.choices[0].text
# 		await bot.send_message(chat_id = message.from_user.id, text = answer, reply_markup=await giveButton(lang_code, '2'))
# 	else:
# 		await bot.send_message(chat_id = message.from_user.id, text = await giveText(lang_code, '4'), reply_markup=await giveButton(lang_code, '2'))




# async def back(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.finish()
#     lang_code = await check(message.from_user.id)
#     main_key = await giveButton(lang_code, '1')
#     await bot.send_message(chat_id = message.from_user.id, text = 'Ok', reply_markup=main_key)

# def register_handlers_create(dp: Dispatcher):
#     dp.register_message_handler(back, state='*', commands=['Назад'])
#     dp.register_message_handler(back, text=back_buttons, state='*')
#     dp.register_message_handler(about_bot, text=rec_tips_buttons, state='*')
#     dp.register_message_handler(find_answer, state=FSMcreate.first_part)