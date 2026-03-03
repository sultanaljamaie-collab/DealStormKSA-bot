import logging
import os

from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.utils.executor import start_webhook

from handlers.start import register_start
from handlers.channel import register_channel
from admin import register_admin

API_TOKEN = os.getenv("BOT_TOKEN")

WEBHOOK_HOST = os.getenv("RENDER_EXTERNAL_URL")
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


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    print("Webhook set:", WEBHOOK_URL)


async def on_shutdown(dp):
    await bot.delete_webhook()


# هذا هو الجزء المهم جداً 👇
async def handle(request):
    update = Update(**await request.json())
    await dp.process_update(update)
    return web.Response()


app = web.Application()
app.router.add_post(WEBHOOK_PATH, handle)


if __name__ == "__main__":
    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
