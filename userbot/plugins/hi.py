import random, re
from SkyhawkBot.utils import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern=r"hi$", outgoing=True))
async def _(event):
    if event.fwd_from:
        await event.edit("""HI HOW ARE YOU""")
        await asyncio.sleep(1)
        await event.edit("""'đşâ¨â¨đşâ¨đşđşđş/nđşâ¨â¨đşâ¨â¨đşâ¨/nđşđşđşđşâ¨â¨đşâ¨/nđşâ¨â¨đşâ¨â¨đşâ¨/nđşâ¨â¨đşâ¨đşđşđş/nâď¸âď¸âď¸âď¸âď¸âď¸âď¸âď¸""")
