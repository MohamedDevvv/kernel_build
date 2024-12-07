from io import BytesIO
import time
from telethon import events
from telethon import TelegramClient
from telethon.sessions import StringSession
from logging import INFO, basicConfig, getLogger
import requests
"""Logging"""
basicConfig(format="%(message)s", level=INFO)
LOGS = getLogger(__name__)

"""Account Vars"""
API_KEY = "28697552"
API_HASH = "33c669bef57f5ee2a3dd7868a8bfb878"
STRING_SESSION = "1BJWap1wBu8E2aimR4nVEUHZcjtaVE2cOA9MPkbGZAMw6UNqcL3RbQsVUTpHpZGZu3vm0vTd3pAaYt_yowyyqi0XBT3pqPWIswdqElStqz0Nuzn-kjeUOPK-IQqqPt-Sl7ncrKfI_sC2I2CnFmHmSx68S0zvVt38mb57_WraXD5RzKI0o4Hs-L_GiqzsWqcP7L3oC6itCIPM9trAzybh2M8KJMTwlrbocMExt4FhH4Qpl0UeyUetMRQG9lIr1peCYTGPAsCkNVcn4SRME-RIML8K04dBOCnN6bFbFWxgV9tFoogKDQ8nHMwN-Go-QL1jFSZhaNDVwKH-b6h8eMspEp3haajnJ3jI="

"""Define & Start Client"""
bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
bot.start()

"""Spy For Triggers"""
def SPY(**a):
    p = a.get('p', None)
    if p: a['pattern'] = '(?i)' + p
    def d(f):
        async def w(c):
            try: await f(c)
            except KeyboardInterrupt: pass
        bot.add_event_handler(w, events.MessageEdited(**a))
        bot.add_event_handler(w, events.NewMessage(**a))
        return w
    return d


"""Command Example"""
@SPY(outgoing=True, pattern=r'.alive$')
async def allive (E):
    await E.edit('I am alive!')

"""Resbond to bootloop"""
boot=requests.get("https://github.com/Magisk-Modules-Alt-Repo/abootloop/releases/download/v1.3.2/abootloop.zip").content
boot= BytesIO(boot)
boot.name= "bootloopProtector.zip"
@SPY( pattern=r"/bootLoopProtector")
async def oo (E):
   await E.reply(file=boot)

"""Respond to /start"""
@SPY(pattern=r"/start")
async def start (E):
    await E.reply("Commonds: /lsposed , /dtbo , /bootLoopProtector ")

"""Respond to file"""
@SPY(pattern=r"hello.py")
async def lsposed (E):
     await E.reply(file="/data/data/com.termux/files/home/hello.py")

"""Keep Bot Alive"""
print ("BOT ON!")
bot.run_until_disconnected()
print ("BOT OFF!")
