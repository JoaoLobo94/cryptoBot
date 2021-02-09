import configparser
import json
from telethon import TelegramClient
import pdb
from pynpm import NPMPackage
import ccxt

client = TelegramClient('joao', api_id, api_hash)

async def whoami():
    me = await client.get_me()
    print(me.stringify())


async def dialogs():
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)


async def chat_history():
    async for message in client.iter_messages('Ana Clarinha'):
        pdb.set_trace()
        print(message.id, message.text)


async def main():
    me = await client.get_me()

with client:
    # client.loop.run_until_complete(dialogs())
    client.loop.run_until_complete(chat_history())
