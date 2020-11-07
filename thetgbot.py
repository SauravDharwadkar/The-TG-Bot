# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import os
import sys
from pathlib import Path
from userbot import Userbot
from userbot.storage import Storage
from telethon.sessions import StringSession

import asyncio
import sys

from aiohttp import web
from telethon import functions

#from .telegram import client, transfer
from web_routes import routes
#from .config import host, port, public_url, tg_bot_token

host="localhost"
port=int( os.environ.get("PORT", "8080"))
public_url="https://"+os.environ.get("TG_APP_NAME",host+":"+port)+".herokuapp.com"

server = web.Application()
server.add_routes(routes)
runner = web.AppRunner(server)

loop = asyncio.get_event_loop()


ENV = bool(os.environ.get("ENV", False))
if ENV:
    from env import ENV
else:
    from env import _ENV as ENV


if ENV.DB_URI is None:
    logging.warning("No DATABASE_URL Found!")
    sys.exit(1)


if len(ENV.SUDO_USERS) >= 0:
    ENV.SUDO_USERS.add("me")

if ENV.SESSION is not None:
    session_name = str(ENV.SESSION)
    userbot = Userbot(
        StringSession(session_name),
        module_path="modules/",
        enviroment=ENV,
        api_id=ENV.APP_ID,
        api_hash=ENV.API_HASH
    )
    loop.run_forever()
    #userbot.run_until_disconnected()
elif len(sys.argv) == 2:
    session_name = str(sys.argv[1])
    userbot = Userbot(
        session_name,
        module_path="modules/",
        connection_retries=None,
        enviroment=ENV,
        api_id=ENV.APP_ID,
        api_hash=ENV.API_HASH
    )
    loop.run_forever()
    #userbot.run_until_disconnected()
else:
    logging.error("USAGE EXAMPLE:\n"
                  "python3 -m thetgbot <SESSION_NAME>"
                  "\nPlease follow the above format to run your userbot."
                  "\nAborting.")
