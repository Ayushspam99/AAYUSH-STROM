import logging
from telethon import TelegramClient
from os import getenv
from STORM.data import DEV

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN", default=None)
BOT_TOKEN2 = getenv("BOT_TOKEN2", default=None)
BOT_TOKEN3 = getenv("BOT_TOKEN3", default=None)
BOT_TOKEN4 = getenv("BOT_TOKEN4", default=None)
BOT_TOKEN5 = getenv("BOT_TOKEN5", default=None)
BOT_TOKEN6 = getenv("BOT_TOKEN6", default=None)
BOT_TOKEN7 = getenv("BOT_TOKEN7", default=None)
BOT_TOKEN8 = getenv("BOT_TOKEN8", default=None)
BOT_TOKEN9 = getenv("BOT_TOKEN9", default=None)
BOT_TOKEN10 = getenv("BOT_TOKEN10", default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="7021594661").split()))
for x in DEV:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="7021594661"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('ᴘʏʀᴏɢʀᴀᴍ x ꜱᴘᴀᴍ 1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('ᴘʏʀᴏɢʀᴀᴍ x ꜱᴘᴀᴍ 2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('ᴘʏʀᴏɢʀᴀᴍ x ꜱᴘᴀᴍ 3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('ᴘʏʀᴏɢʀᴀᴍ x ꜱᴘᴀᴍ 4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('ᴘʏʀᴏɢʀᴀᴍ x ꜱᴘᴀᴍ 5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('ᴘʏʀᴏɢʀᴀᴍ x ꜱᴘᴀᴍ 6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('ᴘʏʀᴏɢʀᴀᴍ x ꜱᴘᴀᴍ 7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('ᴘʏʀᴏɢʀᴀᴍ x ꜱᴘᴀᴍ 8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('ᴘʏʀᴏɢʀᴀᴍ x ꜱᴘᴀᴍ 9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('ᴘʏʀᴏɢʀᴀᴍ x ꜱᴘᴀᴍ 10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
