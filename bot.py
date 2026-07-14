
import os
from dotenv import load_dotenv
import telebot
from google import genai
from google.genai.errors import ServerError
load_dotenv()

# 1. Твои ключи доступа
TG_TOKEN = os.getenv("TG_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_KEY")

# 2. Инициализация бота и клиента Google
bot = telebot.TeleBot(TG_TOKEN)
client = genai.Client(api_key=GEMINI_KEY)

# 3. Создаем чат с памятью. По умолчанию используем лучшую модель
PRIMARY_MODEL = "gemini-3.5-flash"
BACKUP_MODEL = "gemini-2.5-flash"

chat = client.chats.create(model=PRIMARY_MODEL)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Привет! Я твой обновленный ИИ-друг с памятью. Я запомню всё, о чём мы говорим! 😊")

@bot.message_handler(content_types=['text'])
def talk(message):
    global chat
    bot.send_chat_action(message.chat.id, 'typing')
    
    try:
        # Пытаемся отправить сообщение в лучшую модель
        response = chat.send_message(message.text)
    except ServerError as e:
        # Если у Google перегрузка (ошибка 503), тихо переключаемся на резервную модель
        if "503" in str(e) or "UNAVAILABLE" in str(e):
            print("⚠️ Основная модель перегружена. Переключаюсь на резервную...")
            # Пересоздаем чат на резервной модели, сохраняя историю, если это возможно
            chat = client.chats.create(model=BACKUP_MODEL)
            response = chat.send_message(message.text)
        else:
            # Если это какая-то другая ошибка, сообщаем о ней
            raise e

    bot.reply_to(message, response.text)

print("🚀 Бот успешно запущен на бронированной конфигурации!")
bot.infinity_polling()