from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("🔥 أحدث الصفقات"))
    keyboard.add(KeyboardButton("📢 دخول القناة"))
    keyboard.add(KeyboardButton("💎 VIP قريبًا"))
    return keyboard
