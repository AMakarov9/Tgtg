import re
from aiogram import Bot, Dispatcher, executor, types 
from aiogram.types.message import ContentType
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from time import sleep
from tgtg import TgtgClient
from time import gmtime, strftime
import tgtg, asyncio, logging, sqlite3, os, signal, requests
from datetime import datetime
import items
import threading

BOT_TOKEN = '6791600330:AAGH3LH_SN6J7Ts3bTGnQSy3kJSRLdXHL14'
bot = Bot(BOT_TOKEN, parse_mode = "HTML", disable_web_page_preview = True)
dp = Dispatcher(bot)
user_state = dict()
logging.basicConfig (format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

def sendM(id, beskjed): 
    url = f"https://api.telegram.org/{bot}/sendMessage?chat_id={id}&text={beskjed}"
    requests.get(url)


def get_tokens(emaila: str): 
    # Tokens are always new for each session. 
    client = TgtgClient(email = emaila)
    credentials = client.get_credentials()
    client = TgtgClient(access_token=credentials["access_token"], refresh_token=credentials["refresh_token"], user_id=credentials["user_id"], cookie=credentials["cookie"])
    return client

def get_available_items(client: TgtgClient):
#def get_available_items():
    tid = strftime("%H:%M", gmtime())
    logging.info("Checking for available bags at %s", tid)
    items = client.get_items()
    #itemTest = items
    ute = []
    for i in items: 
        if len(i) > 12: 
            if i['in_sales_window'] and i['items_available'] > 0: 
                ute.append(i['store']['store_name'])
                logging.info(f"Added {i['store']['store_name']}")
    
    if len(ute) == 0: 
        logging.info("No bags available")
        return False
    else: 
        return ute
        


@dp.message_handler(commands = 'start')
async def command_start(message: types.Message):
    # if message.chat.id == 1778925351: 
    user_state[message.chat.id] = 'start'
        #logging.info("Checked available bags - svar is: " + str(svar))
    with sqlite3.connect('db.db') as c: 
        row = c.execute('SELECT * FROM user WHERE chat_id=?', (message.chat.id,)).fetchone()
        if row == None: 
            c.execute('INSERT INTO user (chat_id, first_name) VALUES (?, ?)', (message.chat.id, message.chat.first_name))
            await message.answer (text = "You have been added as user and will receive notification.")

    
HELP_COMMAND = '''
/start - Notification when bag available
/help - All commands
''' 
@dp.message_handler(commands='help')
async def help_command(message: types.Message): 
    user_state[message.chat.id] = 'help'

    await message.reply(text=HELP_COMMAND)

# @dp.message_handler(commands = 'status')
# async def command_status(message: types.Message): 
#     user_state[message.chat.id] = 'status'
#     await message.reply(text=f"{currentAvail} available")

async def searchingBags():  
    currentOut = [] 
    while True: 
        await asyncio.sleep(10)
        #availableBags = get_available_items(client)
        availableBags = items.items
        logging.info("Fetching available bags.")
        if availableBags: 
            for i in availableBags: 
                if i not in currentOut: 
                    tid = datetime.now().strftime("%H:%M:%S")
                    with sqlite3.connect('db.db') as c: 
                        rows = c.execute("SELECT chat_id FROM user").fetchall()
                    for row in rows: 
                        try: 
                            i = i['store']['store_name']
                            print(i)
                            sendM(row[0], f"{i} {tid}")
                            #await bot.send_message(chat_id = row[0], text = f"{i} {tid}")
                        except Exception as error: 
                            print(error) 
            currentOut = availableBags
        else: 
            currentOut = []

def runSearchBags(): 
    print("searching bags")
    asyncio.run(searchingBags())

def signal_handler(sig, frame): 
    def force_exit(): 
        print("Forcing stop of program")
        os.kill(os.getpid(), signal.SIGILL)
    force_exit()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    thread = threading.Thread(target = runSearchBags)
    thread.start()
    executor.start_polling(dp)
 
    
 
