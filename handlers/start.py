from aiogram import types
from aiogram.dispatcher import Dispatcher
from database import add_user
from keyboards.main_menu import main_keyboard

async def start_command(message: types.Message):
    add_user(message.from_user.id)

    await message.answer(
        "👋 أهلاً بك في DealStorm KSA\n\n"
        "🔥 أقوى الصفقات اليومية في السعودية\n"
        "💰 نوفر عليك البحث ونجيب لك الأفضل\n\n"
        "اختر من القائمة 👇",
        reply_markup=main_keyboard
    )

def register_start(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start"])
