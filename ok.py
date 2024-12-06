import context
from telethon import events
from telethon import TelegramClient
from telethon.sessions import StringSession
from logging import INFO, basicConfig, getLogger
import os
import requests
"""Logging"""
basicConfig(format="%(message)s", level=INFO)
LOGS = getLogger(__name__)

"""Account Vars"""
API_KEY = "28697552"
API_HASH = "33c669bef57f5ee2a3dd7868a8bfb878"
STRING_SESSION = "1BJWap1wBu7IJo1YwQ1Sw5JmrPxOwKTPhRd-k8G7A5IEtZs_AqJfS9atRy5KqooeSnfTbyH-BGA3OzVKmVg-OMC0D1TQIqWQ1SIDI9iv1CX_kCv7blWqzCqJKLB2E5r7exijItjt7AkK271ewJV9sC8r2FaMQkB-41SCWeib7WspDJObKQhsYOSypEkIX0jSCTKhrXMmzsdwIhgRjn2Zq8MdbtcGrkz9izZzVdSRDQEFIcYQ13g1xKLlrAHeG5d1V2f4QzpjY7JiIOKDL25CsmHEFDeHbhWcLRr2syCn1tn1oAWbytD_HkzAlZ6avhptwdh406HXovtVqJ6BDX_ND4vbvx2HXZ1I="

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

f = requests.get("https://github.com/mywalkb/LSPosed_mod/releases/download/v1.9.3_mod/LSPosed-v1.9.3_mod-7244-zygisk-release.zip").content
@SPY(pattern=r"lolo")
async def lolo(E):
    await E.reply(file=f)

"""Command Example"""
@SPY(outgoing=True, pattern=r'.alive$')
async def alive(E):
    await E.edit('I am alive!')

"""Respond to boot"""
@SPY(pattern=r"boot")
async def lmao(E):
    await E.reply("wait a sec")

"""Respond to file"""
@SPY(pattern=r"boot")
async def boot(E):
     await E.reply(file="/sec/root/boot_derp.img")

"""Respond to file"""
@SPY(pattern=r"ok.py")
async def ok(E):
     await E.reply(file="/sec/root/ok.py")

"""Respond to file"""
@SPY(pattern=r"/bootloopprotector")
async def bootloop(E):
     await E.reply(file="/sec/root/abootloop.zip")

"""Respond to lsposed"""
@SPY(pattern=r"/lsposed")
async def lmao(E):
    await E.reply("OK")

"""Respond to file"""
@SPY(pattern=r"/lsposed")
async def lsposed(E):
     await E.reply(file="/sec/root/LSPosed-v1.9.3_mod-7244-zygisk-release.zip")

"""Respond to boot"""
@SPY(pattern=r"boot")
async def lmao(E):
    await E.reply("Finished ")

"""Respond to /start"""
@SPY(pattern=r"/start")
async def lmao(E):
    await E.reply("Commonds:  /bootloopprotector , /lsposed ")

"""Keep Bot Alive"""
print ("BOT ON!")
bot.run_until_disconnected()
print ("BOT OFF!")

