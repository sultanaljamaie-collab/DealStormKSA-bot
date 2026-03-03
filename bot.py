import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.dispatcher.webhook import WebhookRequestHandler
from aiohttp import web

from handlers.start import register_start
from handlers.channel import register_channel
from admin import register_admin

API_TOKEN = os.getenv("BOT_TOKEN")

WEBHOOK_HOST = "https://dealstormksa-bot.onrender.com"
WEBHOOK_PATH = f"/webhook/{API_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = int(os.getenv("PORT", 10000))

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# تسجيل الهاندلرز
register_start(dp)
register_channel(dp)
register_admin(dp)


async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)
    print("Webhook set:", WEBHOOK_URL)


async def on_shutdown(app):
    await bot.delete_webhook()


app = web.Application()

# 👇 هذا هو الجزء المهم جداً
handler = WebhookRequestHandler(dispatcher=dp, bot=bot)
handler.register(app, path=WEBHOOK_PATH)

app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)

if __name__ == "__main__":
    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
