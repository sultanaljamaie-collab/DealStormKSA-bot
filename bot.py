import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("🔥 أحدث الصفقات"))
keyboard.add(KeyboardButton("📢 دخول القناة"))
keyboard.add(KeyboardButton("💎 VIP قريبًا"))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(
        "👋 أهلاً بك في DealStorm KSA\n\n"
        "🔥 أقوى الصفقات اليومية في السعودية\n"
        "💰 نوفر عليك البحث ونجيب لك الأفضل\n\n"
        "اختر من القائمة 👇",
        reply_markup=keyboard
    )

@dp.message_handler(lambda message: message.text == "📢 دخول القناة")
async def channel(message: types.Message):
    await message.reply("انضم للقناة 👇\nhttps://t.me/DealStorm_KSA")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
