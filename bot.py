import random
import asyncio
from flask import Flask, request
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
async def run_bot():
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
    await application.run_polling()

# Запуск Flask и бота в одном цикле событий
async def run_app():
    # Запуск Flask в отдельном потоке
    from waitress import serve
    import threading

    def start_flask():
        serve(app, host='0.0.0.0', port=10000)

    flask_thread = threading.Thread(target=start_flask)
    flask_thread.start()

    # Запуск бота
    await run_bot()

if __name__ == '__main__':
    # Запуск приложения
    asyncio.run(run_app())
