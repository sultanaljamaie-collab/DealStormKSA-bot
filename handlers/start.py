from aiogram import types
from aiogram.dispatcher import Dispatcher
from keyboards.main_menu import main_keyboard

async def start_handler(message: types.Message):
    await message.reply(
        "👋 أهلاً بك في DealStorm KSA\n\n"
        "🔥 أقوى الصفقات اليومية في السعودية\n"
        "💰 نوفر عليك البحث ونجيب لك الأفضل\n\n"
        "اختر من القائمة 👇",
        reply_markup=main_keyboard()
    )

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
