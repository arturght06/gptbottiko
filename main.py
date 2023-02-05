from config import admin_id_list
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import keyboard
from create_bot import bot, dp
from connect import saveOneToJson, saveAllToJson

# send message to admins from list about starting bot
async def send_admin(dp):
	print(await saveAllToJson())
	for i in admin_id_list:
		await bot.send_message(chat_id = i, text = "Bot was started")


# import all handlers files
from handlers import settings, admin, faq, search

# register handlers
settings.register_handlers_settings(dp)
faq.register_handlers_create(dp)
search.register_handlers_create(dp)
admin.register_handlers_create(dp)


executor.start_polling(dp, on_startup=send_admin, skip_updates=True)