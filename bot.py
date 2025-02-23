import random
import threading
import asyncio
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Создаем Flask-приложение
app = Flask(__name__)

@app.route('/')
def home():
    return "Telegram Bot is running!"

# Команда /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Привет! Я бот для игры в орёл или решка. Напиши 'орёл или решка', и я выберу случайное число: +1, +10, -10 или -1.")

# Обработка фразы "орёл или решка"
async def flip_on_message(update: Update, context: CallbackContext) -> None:
    if "орёл или решка" in update.message.text.lower():
        result = random.choice(["+1", "+10", "-10", "-1"])
        await update.message.reply_text(f"Результат: {result}")

# Команда /reset
async def reset(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Бот сброшен. Напиши 'орёл или решка', чтобы начать заново.")

# Функция для запуска бота
def run_bot():
    # Вставьте сюда ваш токен
    token = "7598790657:AAHZg02aPDKJN3waFGnek0SLhsEnEKNGMPc"
    
    # Создаем приложение
    application = Application.builder().token(token).build()

    # Регистрация команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("reset", reset))

    # Регистрация обработчика сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, flip_on_message))

    # Запуск бота
    print("Бот запущен...")
    
    # Создаем новый цикл событий для асинхронного кода
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    # Запускаем бота в цикле событий
    loop.run_until_complete(application.run_polling())

if __name__ == '__main__':
    # Запуск бота в отдельном потоке
    threading.Thread(target=run_bot).start()
    
    # Запуск Flask на порту 10000
    app.run(host='0.0.0.0', port=10000)
