from aiogram import types
from aiogram.dispatcher import Dispatcher

async def channel_handler(message: types.Message):
    if message.text == "📢 دخول القناة":
        await message.reply("انضم للقناة 👇\nhttps://t.me/DealStorm_KSA")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(channel_handler)
