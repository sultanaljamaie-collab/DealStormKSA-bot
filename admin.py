from aiogram import types
from aiogram.dispatcher import Dispatcher
from database import get_all_users

ADMIN_ID = 1330477563

async def admin_panel(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("🔐 لوحة التحكم:\n\n/send اكتب رسالتك لإرسالها للجميع\n/users لعرض عدد المستخدمين")

async def broadcast(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        text = message.get_args()
        users = get_all_users()
        count = 0

        for user in users:
            try:
                await message.bot.send_message(user[0], text)
                count += 1
            except:
                pass

        await message.answer(f"✅ تم الإرسال إلى {count} مستخدم")

async def user_count(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        users = get_all_users()
        await message.answer(f"👥 عدد المستخدمين: {len(users)}")

def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_panel, commands=["admin"])
    dp.register_message_handler(broadcast, commands=["send"])
    dp.register_message_handler(user_count, commands=["users"])
