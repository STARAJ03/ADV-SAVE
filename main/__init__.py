#Join me at telegram @dev_gagan

from pyrogram import Client
from pyromod import listen
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "27765349" #config("API_ID", default=None, cast=int)
API_HASH = "9df1f705c8047ac0d723b29069a1332b" #config("API_HASH", default=None)
BOT_TOKEN = "7779351596:AAFuSwUpssu4Nt9kf-yk_sIJu1trPudmShI" #config("BOT_TOKEN", default=None)
SESSION = "BQHDMOUAIOGZHesmwkhKztZ1bU7NokB1HVLtNKHAnr35ElBp-FQ7IPkvayF0s5JoOGLN44ksi4kqeUNxnG56Vd8Mh_2Lo3ICHSN2J2u0WyYIOj96FBxN2gq_iekABQkL-vdXTB1DrOswqzBJBG9RaGPFVoiEYDAd0iD2vqgT3x2wOz98gBZNKPCGpWQYbGR6GKe66W5SRZRlLWJaEDQcTEIxNF48nIEGW7cwK2AG3eR4-iyVg5Zxaje_ACeNuCN5kLtQsNkGEV23f7-EdLQTG1zKnZ57AjUvYQdJ7o1pdGhkKknUUmOcfG4xn42RbHUwccqD1CmsGLU5Zh-vTbgBGh9AiP79HAAAAAGlHSMFAA" #config("SESSION", default=None)
FORCESUB = "checking123456789" #config("FORCESUB", default=None)
AUTH = "1116405290" #config("AUTH", default=None)
SUDO_USERS = [1116405290]

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
