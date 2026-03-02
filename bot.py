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


# ====== Webhook Settings ======

WEBHOOK_HOST = "https://dealstormksa-bot.onrender.com"
WEBHOOK_PATH = f"/webhook/{API_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

PORT = int(os.environ.get("PORT", 10000))


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    await bot.delete_webhook()


if __name__ == '__main__':
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host="0.0.0.0",
        port=PORT,
    )
