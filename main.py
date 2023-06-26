
import logging

import wikipedia
wikipedia.set_lang('uz')
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6110125167:AAEbEYd1ji5LxkfTGH8Qyt1Vhn3CjZu0BXg'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help','stop'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom!\nWikipedia botga xush kelibsiz!\n")


#
# @dp.message_handler()
# async def sendWiki(message: types.Message):
#        try:
#            respond = wikipedia.summary(message.text)
#            await message.reply(respond)
#        except:
#            await message.reply("Bu mavzuga oid maqola topilmadi!")
@dp.message_handler()
async def sendWiki(message:types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.reply(respond)
    except:
        await message.reply("Bu mavzuga oid maqola topilmadi!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
