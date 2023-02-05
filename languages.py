from connect import check

arrOfLanguages = ['uk', 'en']
allNamesOfLangs = {'uk': 'Українська','en': 'English'}

standart_lang = 'en'

arrOfPhrases = { 

'uk': {
'1': '''<b>Ласкаво просимо до нашого кулінарного бота! 🫶</b>


<b>Коротенько про "Kitchen Helper Bot":</b>
🔸Ми тут, щоб допомогти вам знайти <b>ідеальний рецепт</b> для будь-якої події.
Незалежно від складності страви, наш бот вам допоможе. 
У нас є тисячі рецептів з усього світу, тому ви можете досліджувати і знаходити щось нове кожного разу.
<b>Давайте починати готувати!😉</b>

⚒ <i>Від команди <b>Black Wolf</b></i>''', 
'2': '''<b>"Kitchen Helper Bot"</b> - це ваш помічник на кухні😉

За допомогою простого інтерфейсу ви можете швидко знайти ідеальний рецепт для будь-якої події. 
Бот також надає по-кроковий опис для кожного рецепту, так що навіть недосвідчені кулінари можуть досягти успіху в кухні. Завдяки широкому вибору рецептів, цей бот завжди буде корисним для домашніх кулінарів.❤️

<i>Від команди Black Wolf</i>💎''',
'3': '''Щоб обрати мову напишіть її номер👇\n''',
'4': '''<i><b>Щось не так🤔\nСпробуй ще раз❗️</b></i>''',
'5': '''✅ Мову змінено''',
'6': '''🔘 Що тебе цікавить?

Можеш написати будь-яке питання стосовно приготування або рецепту, а я якнайшвидше спробую тобі відповісти. Щоб точно отримати ту відповідь, яку очікуєш, то розпиши все точно, наприклад:

❌ <i>Як приготувати суп
✅ Напиши по-кроково як приготувати пиріжки без дріжджів з сухим тістом</i>

<i>Перепрошую, але можливі помилки у відповіді</i>''',
},


'en': {
'1': '''<b>Welcome to our culinary bot! </b>🫶

<b>A brief introduction to "Kitchen Helper Bot"</b>:
🔸We are here to help you find the <b>perfect recipe</b> for any occasion. 
No matter the complexity of the dish, our bot will help you out. 
We have thousands of recipes from all over the world, so you can explore and find something new every time. 
<b>Let's get cooking!</b>😉

⚒ <i>From the <b>Black Wolf</b> team</i>''',
'2': '''<b>"Kitchen Helper Bot"</b> - is your kitchen assistant😉

With its simple interface, you can quickly find the perfect recipe for any occasion. The bot also provides step-by-step instructions for each recipe, so even inexperienced cooks can succeed in the kitchen. With its wide selection of recipes, this bot will always be useful for home cooks.❤️

<i>From the Black Wolf team</i>''',
'3': '''To select a language, write its number👇\n''',
'4': '''<i><b>Something is not right🤔 Try again❗️</b></i>''',
'5': '''✅ Language changed''',
'6': '''What interests you?

You can write any question about cooking or a recipe and I will try to answer you as soon as possible. To get the exact answer you expect, be as specific as possible, for example:

❌ <i>How to cook soup
✅ Please explain step by step how to make pies without raisins with dry dough</i>

<i>I apologize in advance for any possible mistakes in the answer</i>''',


}
}


async def giveText(lang_code, number):
	if lang_code in arrOfLanguages:
		return arrOfPhrases[lang_code][number]
	else:
		return arrOfPhrases[standart_lang][number]

