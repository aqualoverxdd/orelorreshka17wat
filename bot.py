import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Команда /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Привет! Я бот для игры в орёл или решка. Напиши 'орёл или решка', и я выберу случайное число: +1, +10, -10 или -1.")

# Обработка фразы "орёл или решка"
async def flip_on_message(update: Update, context: CallbackContext) -> None:
    if "орёл или решка" in update.message.text.lower():
        result = random.choice(["+10", "-10"])
        await update.message.reply_text(f"Результат: {result}")

# Команда /reset
async def reset(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Бот сброшен. Напиши 'орёл или решка', чтобы начать заново.")

def main() -> None:
    # Вставьте сюда ваш токен
    token = "7598790657:AAHZg02aPDKJN3waFGnek0SLhsEnEKNGMPc"
    
    # Создаем приложение
    application = Application.builder().token(token).build()  # Обратите внимание на строчную букву

    # Регистрация команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("reset", reset))

    # Регистрация обработчика сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, flip_on_message))

    # Запуск бота
    print("Бот запущен...")
    application.run_polling()  # Используем application, а не Application

if __name__ == '__main__':
    main()
