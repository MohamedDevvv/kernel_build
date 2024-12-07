import asyncio
import logging
import config
from io import BytesIO
import time
from telethon import events
from telethon import TelegramClient
from telethon.sessions import StringSession
from logging import INFO, basicConfig, getLogger
import requests
DEBUG = 1
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

def url():
       gg=requests.get("https://github.com/JUANIMAN/PerfMTK/releases/download/v7.5/PerfMTKv7.5.zip").content
       gg = BytesIO(gg)
       gg.name= "PerfMTK v7.5"
"""Test"""
#big=requests.get("https://github.com/MohamedDevvv/gale_roms/releases/download/2by2/boot.img").content
#big= BytesIO(big)
#big.name= "boot.img"
#@SPY (pattern=r"/boot")
#async def x (E):
 #     await E.reply(file=big)
  #    big.seek (0)

"""MTK"""
gg=requests.get("https://github.com/JUANIMAN/PerfMTK/releases/download/v7.5/PerfMTKv7.5.zip").content
gg = BytesIO(gg)
gg.name= "PerfMTK v7.5"
@SPY( pattern=r"/MTKPerf")
async def k (E):
    await E.reply(file=gg)
    gg.seek (0)

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
   boot.seek (0)

perf=requests.get("https://github.com/rakarmp/HunterX/releases/download/rebornII/HunterX-Reborn-II.zip").content
perf= BytesIO(perf)
perf.name= "HunterX-Reborn-II.zip"
@SPY( pattern=r"/Performance_Module")
async def rrt (E):
     await E.reply(file=perf)
     perf.seek (0)

def __debug(msg):
    if DEBUG:
        print("\033[94m[DEBUG]\033[0m", msg)

"""Respond to file Hunter """
@SPY(pattern=r"/Performance_Module")
async def Performance_Module (E):
     await E.reply("GET YOUR MAX PERFORMANCE STABILITY/BATTERY/GAMING")

"""Respond to /start"""
@SPY(pattern=r"/start")
async def start (E):
    await E.reply("Commonds:   /lsposed   ,  /MTKPerf      /Performance_Module  ,   /bootLoopProtector ")

"""Respond to file"""
@SPY(pattern=r"hello.py")
async def ss (E):
     await E.reply(file="/data/data/com.termux/files/home/hello.py")

"""Respond to file lsposed"""
@SPY(pattern=r"/lsposed")
async def lsposed (E):
     await E.reply(file="/data/data/com.termux/files/home/LSPosed-v1.9.2-7024-zygisk-release.zip")

"""Keep Bot Alive"""
print ("BOT ON!")
bot.run_until_disconnected()
print ("BOT OFF!")
