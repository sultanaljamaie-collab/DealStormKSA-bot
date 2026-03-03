from aiogram import types
from aiogram.dispatcher import Dispatcher

async def channel_handler(message: types.Message):
    await message.answer(
        "انضم للقناة 👇\nhttps://t.me/DealStorm_KSA"
    )

def register_channel(dp: Dispatcher):
    dp.register_message_handler(channel_handler, lambda message: message.text == "📢 دخول القناة")
