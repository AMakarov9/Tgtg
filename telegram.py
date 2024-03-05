import re
from aiogram import Bot, Dispatcher, executor, types 
from aiogram.types.message import ContentType
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
import logging
import test
from time import sleep
from get_client import get_tokens

logging.basicConfig (format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)


# PASTE TELEGRAM BOT TOKEN FROM BOTFATHER 
BOT_TOKEN = ''


bot = Bot(BOT_TOKEN, parse_mode = "HTML", disable_web_page_preview = True)
dp = Dispatcher(bot)

user_state = dict()

# Message.chat.id is my personal id. Put it in to prevent potential spam (?). 

@dp.message_handler(commands = 'start')
async def command_start(message: types.Message):
    # if message.chat.id == 1778925351: 
    user_state[message.chat.id] = 'start'
    await message.answer (
        text = 'Send /email'
    )

@dp.message_handler(commands = 'email')
async def worker(message: types.Message):

    #if message.chat.id == 1778925351: 
    user_state[message.chat.id] = 'email'
    await message.answer (
        text = 'Send your email please'
    )    


@dp.message_handler(content_types = ContentType.TEXT)
async def message(message: types.Message):
    # if message.chat.id == 1778925351: 
    epost = message.text
    match user_state[message.chat.id]:
        
        case "email": 
            pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

            if re.match(pattern, message.text) is not None:
                await message.answer (
                    text = f'Verification passed'
                )

                client = get_tokens(message.text)
                alleRegistrerte = []
                while True: 
                    sleep(10)
                    svar = test.run(client, alleRegistrerte)
                    if svar: await message.answer(text=svar)

            else:
                await message.answer (
                    text = f'Verification failed'
                )
                await message.answer (
                    text = f'This is the wrong mail: {message.text}'
                )
            user_state[message.chat.id] = None


if __name__ == '__main__':
    executor.start_polling(dp)
        