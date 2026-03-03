import logging
import os

from aiogram import Bot, Dispatcher, executor

# استدعاء التسجيلات
from handlers.start import register_start
from handlers.channel import register_channel
from admin import register_admin

# تحميل التوكن من متغير البيئة
API_TOKEN = os.getenv("BOT_TOKEN")

# تفعيل اللوج
logging.basicConfig(level=logging.INFO)

# إنشاء البوت
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def register_handlers():
    register_start(dp)
    register_channel(dp)
    register_admin(dp)


if __name__ == "__main__":
    register_handlers()
    executor.start_polling(dp, skip_updates=True)
