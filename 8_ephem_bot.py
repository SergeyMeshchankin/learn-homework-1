"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

* Используется версия python-telegram-bot v22.0

"""
import logging
import setting
import ephem

from datetime import datetime
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


async def greet_user(update, context):
    await update.message.reply_text("Привет! Я бот-астроном. Используй /planet <название планеты>")


async def talk_to_me(update, context):
    await update.message.reply_text("Я понимаю только команду /planet")


async def planet_command(update, context):
    command_parts = update.message.text.split()

    if len(command_parts) < 2:
        await update.message.reply_text("Пример команды: /planet Mars")
        return

    planet_name = command_parts[1].capitalize()
    today = datetime.now().strftime("%Y/%m/%D")

    if hasattr(ephem, planet_name):
        planet = getattr(ephem, planet_name)(today)
        constellation = ephem.constellation(planet)[1]
        await update.message.reply_text(f"{planet_name} сегодня в созвездии {constellation}")
    else:
        await update.message.reply_text("Такую планету я не знаю")


def main():
    mybot = ApplicationBuilder().token(setting.API_KEY).build()

    mybot.add_handler(CommandHandler("start", greet_user))
    mybot.add_handler(CommandHandler("planet", planet_command))
    mybot.add_handler(MessageHandler(filters.TEXT, talk_to_me))

    mybot.run_polling()


if __name__ == "__main__":
    main()
