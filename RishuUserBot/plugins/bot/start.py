from RishuUserBot import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    "╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ──── ⚘\n┆⚘ ʜᴇʏ, ɪ ᴀᴍ : [˹ 🅤sᴇʀʙᴏᴛ ˼](t.me/ur_rishu_143)\n┆⚘ ᴍᴏʀᴇ ᴀɴɪᴍᴀᴛɪᴏɴ,ғᴜɴ\n┊⚘ ᴘᴏᴡᴇʀғᴜʟ & ᴜsᴇғᴜʟ ᴜsᴇʀʙᴏᴛ\n╰───────────────────────\n❍ нσɯ тσ υʂҽ тнιʂ вσᴛ - [ᴛɪᴘs ʜᴇʀᴇ](https://t.me/rishututorial) \n❍ ʂҽʂʂισɳʂ ɠҽɳ вσᴛ ⁚ [sparsh-ʙᴏᴛ](https://t.me/SILENT_HEARTS_SH) \n────────────────────────\n❍ ¢ℓσɳҽ вσт ⁚ /clone [ ʂᴛɾιɳg ʂҽʂʂισɳ ]\n────────────────────────\n❍ ᴘσɯҽɾҽᴅ ʙу ⏤‌‌‌‌  [˹sparsh ʙσᴛ](https://t.me/SILENT_HEARTS_SH) \n────────────────────────"
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("˹ ᴏᴡɴᴇʀ ˼", url="https://t.me/HYE_BABU"),
                InlineKeyboardButton("˹ ᴜᴘᴅᴀᴛᴇ ˼", url="https://t.me/SILENT_HEARTS_SH"),
            ],
            [
                InlineKeyboardButton("˹ sᴜᴘᴘᴏʀᴛ ˼", url="https://t.me/SILENT_HEARTS_SH"),
                InlineKeyboardButton("˹ ᴄʜᴧᴛ ʙσᴛ ˼", url="https://t.me/SILENT_HEARTS_SH"),
            ],
            [ 
                InlineKeyboardButton("˹ ʀєᴘσ ˼", url="https://t.me/SILENT_HEARTS_SH"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("ᴜsᴀɢᴇ:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("🎨 ᴘʀᴏᴄᴇssɪɴɢ.....✲")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="RishuUserBot/plugins"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f" Successfully host 🎨 {user.first_name} 💨.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
