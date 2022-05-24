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

import psutil
from pyrogram import Client
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import Message
from pytgcalls import __version__ as pytover

from Codexun import (BOT_ID, BOT_NAME, SUDO_USERS, app)
from Codexun import client as userbot
from Codexun.database.chats import get_served_chats
from Codexun.database.sudo import get_sudoers
from Codexun.database.ping import get_readable_time


