from keyboard import *
from aiogram import Dispatcher
from create_bot import dp, bot 
from config import admin_id_list
from languages import *
from connect import check, write_update_lang, saveOneToJson

photo_link = 'https://cdn.discordapp.com/attachments/1008571184729825300/1070104438116728842/Privalie6_cooking_d124022a-ca21-4aa9-9548-24d93239d800.png'

async def process_hi_command(message):

    for i in admin_id_list:
        await bot.send_message(chat_id=i,  text=str(f'LOG --- Такой пользователь запустил бота{message.from_user}'))

    status_check_lang = await check(message.from_user.id)
    if status_check_lang == False:
    	lang_code = message.from_user.language_code
    	user_id = str(message.from_user.id)
    	await write_update_lang(user_id, lang_code)
    	await saveOneToJson(user_id, lang_code)
    else:
    	lang_code = status_check_lang

    await bot.send_photo(chat_id=message.from_user.id, photo=photo_link, caption=await giveText(lang_code,'1'), reply_markup=await giveButton(lang_code, "1"))


def register_handlers_settings(dp: Dispatcher):
    dp.register_message_handler(process_hi_command, text = back_buttons)
    dp.register_message_handler(process_hi_command, commands=["start"])