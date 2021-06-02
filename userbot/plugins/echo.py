# Echo remastered by @Kraken_The_BadAss for hellbot
# Codes by @mrconfused
# Kang with credits

import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from userbot import CMD_HELP
from userbot.plugins.sql_helper.echo_sql import (
    addecho,
    get_all_echos,
    is_echo,
    remove_echo,
)
from SkyhawkBot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="echo$"))
@bot.on(sudo_cmd(pattern="echo$", allow_sudo=True))
async def echo(Skyhawk):
    if Skyhawk.fwd_from:
        return
    if Skyhawk.reply_to_msg_id is not None:
        reply_msg = await Skyhawk.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = Skyhawk.chat_id
        try:
            aura = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            aura = Get(aura)
            await Skyhawk.client(aura)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await edit_or_reply(Skyhawk, "The user is already enabled with echo ")
            return
        addecho(user_id, chat_id)
        await edit_or_reply(Skyhawk, "Hii....😄🤓")
    else:
        await edit_or_reply(Skyhawk, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="rmecho$"))
@bot.on(sudo_cmd(pattern="rmecho$", allow_sudo=True))
async def echo(Skyhawk):
    if Skyhawk.fwd_from:
        return
    if Skyhawk.reply_to_msg_id is not None:
        reply_msg = await Skyhawk.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = Skyhawk.chat_id
        try:
            aura = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            aura = Get(aura)
            await Skyhawk.client(aura)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await edit_or_reply(Skyhawk, "Echo has been stopped for the user")
        else:
            await edit_or_reply(Skyhawk, "The user is not activated with echo")
    else:
        await edit_or_reply(Skyhawk, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="listecho$"))
@bot.on(sudo_cmd(pattern="listecho$", allow_sudo=True))
async def echo(Skyhawk):
    if Skyhawk.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "echo enabled users:\n\n"
        for echos in lsts:
            output_str += (
                f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "No echo enabled users "
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"echo enabled users: [here]({url})"
        await edit_or_reply(Skyhawk, reply_text)
    else:
        await edit_or_reply(Skyhawk, output_str)


@bot.on(events.NewMessage(incoming=True))
async def samereply(Skyhawk):
    if Skyhawk.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    if is_echo(Skyhawk.sender_id, Skyhawk.chat_id):
        await asyncio.sleep(2)
        try:
            aura = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            aura = Get(aura)
            await Skyhawk.client(aura)
        except BaseException:
            pass
        if Skyhawk.message.text or Skyhawk.message.sticker:
            await Skyhawk.reply(Skyhawk.message)


CmdHelp("echo").add_command(
  'echo', 'Reply to a user', 'Replays every message from whom you enabled echo'
).add_command(
  'rmecho', 'reply to a user', 'Stop replayings targeted user message'
).add_command(
  'listecho', None, 'Shows the list of users for whom you enabled echo'
).add()