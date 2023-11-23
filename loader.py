from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN

from aiogram import Bot, Dispatcher


bot = Bot(BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
