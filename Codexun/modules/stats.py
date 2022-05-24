import asyncio
import json
import logging
import platform
import re
import socket
import time
import uuid
from datetime import datetime
from sys import version as pyver

from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)
from Codexun import BOT_NAME, BOT_USERNAME

import psutil
from pyrogram import Client
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import Message
from pytgcalls import __version__ as pytover

from Codexun import (BOT_ID, BOT_NAME, SUDO_USERS, app, boottime)
from Codexun import client as userbot
from Codexun.database.chats import get_served_chats
from Codexun.database.sudo import get_sudoers
from Codexun.database.ping import get_readable_time

def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ ᴜᴘᴛɪᴍᴇ", callback_data="UPT"),
            InlineKeyboardButton(text="💾 ʀᴀᴍ", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 ᴄᴘᴜ", callback_data="CPT"),
            InlineKeyboardButton(text="💽 ᴅɪsᴋ", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 ʙᴀᴄᴋ", callback_data="settingm")],
    ]
    return f"🔧  **{BOT_NAME} Settings**", buttons


stats1 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="sʏsᴛᴇᴍ sᴛᴀᴛs", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="sᴛᴏʀᴀɢᴇ sᴛᴀᴛs", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʙᴏᴛ sᴛᴀᴛs", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="ᴀssɪsᴛᴀɴᴛ sᴛᴀᴛs", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="ɢᴇɴᴇʀᴀʟ sᴛᴀᴛs", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="sᴛᴏʀᴀɢᴇ sᴛᴀᴛs", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʙᴏᴛ sᴛᴀᴛs", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="ᴀssɪsᴛᴀɴᴛ sᴛᴀᴛs", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats3 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="sʏsᴛᴇᴍ sᴛᴀᴛs", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="ɢᴇɴᴇʀᴀʟ sᴛᴀᴛs", callback_data=f"gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʙᴏᴛ sᴛᴀᴛs", callback_data=f"bot_stats"
            ),            
            InlineKeyboardButton(
                text="ᴀssɪsᴛᴀɴᴛ sᴛᴀᴛs", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats4 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="sʏsᴛᴇᴍ sᴛᴀᴛs", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="sᴛᴏʀᴀɢᴇ sᴛᴀᴛs", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ɢᴇɴᴇʀᴀʟ sᴛᴀᴛs", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="ᴀssɪsᴛᴀɴᴛ sᴛᴀᴛs", callback_data=f"assis_stats"
            )
        ],
    ]
)


stats5 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="sʏsᴛᴇᴍ sᴛᴀᴛs", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="sᴛᴏʀᴀɢᴇ sᴛᴀᴛs", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʙᴏᴛ sᴛᴀᴛs", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="ɢᴇɴᴇʀᴀʟ sᴛᴀᴛs", callback_data=f"gen_stats"
            )
        ],
    ]
)


stats6 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="ɢᴇᴛᴛɪɴɢ ᴀssɪsᴛᴀɴᴛ sᴛᴀᴛs....",
                callback_data=f"wait_stats",
            )
        ]
    ]
)

async def bot_sys_stats():
    bot_uptime = int(time.time() - boottime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    stats = f"""
**Uptime:** {get_readable_time((bot_uptime))}
**CPU:** {cpu}%
**RAM:** {mem}%
**Disk: **{disk}%"""
    return stats


@app.on_message(filters.command("stats") & ~filters.edited)
async def gstats(_, message):
    start = datetime.now()
    try:
        await message.delete()
    except:
        pass
    uptime = await bot_sys_stats()
    response = await message.reply_text("Getting Stats!"
    )
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    smex = f"""
[•]<u>**General Stats**</u>
    
Ping: `⚡{resp} ms`
{uptime}
    """
    await response.edit_text(smex, reply_markup=stats1)
    return


@app.on_callback_query(
    filters.regex(
        pattern=r"^(sys_stats|sto_stats|bot_stats|Dashboard|mongo_stats|gen_stats|assis_stats|wait_stats)$"
    )
)
async def stats_markup(_, CallbackQuery):
    command = CallbackQuery.matches[0].group(1)
    if command == "sys_stats":
        await CallbackQuery.answer("Getting System Stats...", show_alert=True)
        sc = platform.system()
        arch = platform.machine()
        ram = (
            str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"
        )
        bot_uptime = int(time.time() - boottime)
        uptime = f"{get_readable_time((bot_uptime))}"
        smex = f"""
[•]<u>**System Stats**</u>

**Uptime:** {uptime}
**System Proc:** Online
**Platform:** {sc}
**Architecture:** {arch}
**Ram:** {ram}
**PyTgCalls Version:** {pytover.__version__}
**Python Ver:** {pyver.split()[0]}
**Pyrogram Ver:** {pyrover}"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats2)
    if command == "sto_stats":
        await CallbackQuery.answer(
            "Getting Storage Stats...", show_alert=True
        )
        hdd = psutil.disk_usage("/")
        total = hdd.total / (1024.0 ** 3)
        total = str(total)
        used = hdd.used / (1024.0 ** 3)
        used = str(used)
        free = hdd.free / (1024.0 ** 3)
        free = str(free)
        smex = f"""
[•]<u>**Storage Stats**</u>

**Storage Avail:** {total[:4]} GiB 
**Storage Used:** {used[:4]} GiB
**Storage Left:** {free[:4]} GiB"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats3)
    if command == "bot_stats":
        await CallbackQuery.answer("Getting Bot Stats...", show_alert=True)
        served_chats = []
        chats = await get_served_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
        sudoers = await get_sudoers()
        modules_loaded = "20"
        j = 0
        for count, user_id in enumerate(sudoers, 0):
            try:
                user = await app.get_users(user_id)
                j += 1
            except Exception:
                continue
        smex = f"""
[•]<u>**Bot Stats**</u>

**Modules Loaded:** {modules_loaded}
**Sudo Users:** {j}
**Served Chats:** {len(served_chats)}"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats4)
    if command == "assis_stats":
        await CallbackQuery.answer(
            "Getting Assistant Stats...", show_alert=True
        )
        await CallbackQuery.edit_message_text(
            "Getting Assistant Stats.. Please Wait...", reply_markup=stats6
        )
        groups_ub = channels_ub = bots_ub = privates_ub = total_ub = 0
        async for i in userbot.iter_dialogs():
            t = i.chat.type
            total_ub += 1
            if t in ["supergroup", "group"]:
                groups_ub += 1
            elif t == "channel":
                channels_ub += 1
            elif t == "bot":
                bots_ub += 1
            elif t == "private":
                privates_ub += 1

        smex = f"""
[•]<u>Assistant Stats</u>

**Dialogs:** {total_ub}
**Groups:** {groups_ub} 
**Channels:** {channels_ub} 
**Bots:** {bots_ub}
**Users:** {privates_ub}"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats5)
    if command == "gen_stats":
        start = datetime.now()
        uptime = await bot_sys_stats()
        await CallbackQuery.answer(
            "Getting General Stats...", show_alert=True
        )
        end = datetime.now()
        resp = (end - start).microseconds / 1000
        smex = f"""
[•]<u>General Stats</u>

**Ping:** `⚡{resp} ms`
{uptime}"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats1)
    if command == "wait_stats":
        await CallbackQuery.answer()
