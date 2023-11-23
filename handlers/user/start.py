from aiogram import Router, types, Bot
from aiogram.filters import CommandStart

from keyboards.inline import menu


start_router = Router()


# Обработчик команды /start
@start_router.message(CommandStart())
async def cmd_start(message: types.Message, bot: Bot):

    image = types.FSInputFile("photo/logo.jpg")
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=image,
        reply_markup=menu.get_menu()
    )
