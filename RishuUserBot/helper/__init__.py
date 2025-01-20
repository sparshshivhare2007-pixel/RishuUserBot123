import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "RishuUserBot"])

async def join(client):
    try:
        await client.join_chat("BABY09_WORLD")
    except BaseException:
        pass
