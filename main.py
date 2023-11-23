import sys

from aiogram.methods import DeleteWebhook

import asyncio

from loader import dp, bot

import logging


async def main() -> None:

    await bot(DeleteWebhook(drop_pending_updates=True))  # Пропуск обновлений, которые были не при работе бота
    from handlers import main_user_router
    dp.include_routers(
        main_user_router
    )
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())