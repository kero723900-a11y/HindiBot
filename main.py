import telebot
from telebot import types

# توكن بوت مملكة الهندي الخاص بك
TOKEN = "8364737917:AAGajq29sgnkUg10rBeI1CvMLS1ib23VN-U"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btns = [
        types.KeyboardButton('🔙 رجوع'),
        types.KeyboardButton('🔝 القائمة الرئيسية'),
        types.KeyboardButton('🎛 محرر الأزرار'),
        types.KeyboardButton('📝 تعديل المشاركات'),
        types.KeyboardButton('🔐 Admin')
    ]
    markup.add(*btns)
    bot.send_message(message.chat.id, "✅ مبروك يا هندي! البوت الآن يعمل من سيرفر دائم 🚀", reply_markup=markup)

if __name__ == "__main__":
    bot.infinity_polling()
  
