from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from languages import standart_lang

button_cancel = KeyboardButton('Назад')
brcs_key = ReplyKeyboardMarkup(resize_keyboard=True).add(button_cancel)

button_search = KeyboardButton('🔎')
button_settings = KeyboardButton('⚙️')
greet_key = ReplyKeyboardMarkup(resize_keyboard=True).add(button_search, button_settings)

button_1_admin = KeyboardButton('IAMHACKER')
admin_key = ReplyKeyboardMarkup(resize_keyboard=True).add(button_1_admin, button_cancel)




back_buttons = ['Назад', 'Back']
rec_tips_buttons = ['Рецепти і поради🔎', 'Recipes & Tips🔎']
about_buttons = ['Про бота📜', 'About bot📜']
change_lang_buttons = ['Змінити мову', 'Change language']
arrOfButtons = { 

'uk': {
'1': ['Рецепти і поради🔎', 'Про бота📜'], 
'2': ['Назад'],
'3': ['Назад', 'Змінити мову'],
},

'en': {
'1': ['Recipes & Tips🔎', 'About bot📜'],
'2': ['Back'],
'3': ['Back', 'Change language'],

}
	
}

async def giveButton(lang_code, number):
	if lang_code in arrOfButtons:
		a = arrOfButtons[lang_code][number]
		# button = KeyboardButton(*a)
		key = ReplyKeyboardMarkup(resize_keyboard=True).add(*a)
		return key
	else:
		a = arrOfButtons[standart_lang][number]
		# button = KeyboardButton(*a)
		key = ReplyKeyboardMarkup(resize_keyboard=True).add(*a)
		return key