# import logging
from pyrogram import Client, idle

api_id = 3164029
api_hash = "d9441a47ed5187616613fb6d61ee0208"

plugins = dict(
    root="plugins",
    include=[
        "vc.player",
        "ping"
    ]
)

app = Client("tgvc", api_id, api_hash, plugins=plugins)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
