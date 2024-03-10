import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from headlers import comand
from headlers import carier_choice
import logging

async def main():
    # Включаем логгирование
    logging.basicConfig(level=logging.INFO)

    # Создаем объект бота
    bot = Bot(token=config.token)

    # Диспечер
    dp = Dispatcher()
    dp.include_router(carier_choice.router)
    dp.include_router(comand.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())