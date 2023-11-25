from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext

from keyboards.inline import menu

go_home_router = Router()


# Обработчик кнопки Меню🏠
@go_home_router.callback_query(F.data == "go_menu")
async def go_start_menu(callback: types.CallbackQuery, state: FSMContext, bot: Bot):

    await callback.message.delete()

    message = await bot.send_photo(
        chat_id=callback.from_user.id,
        photo=types.FSInputFile('photo/load.jpg')
    )

    await state.clear()

    image = types.FSInputFile("photo/logo.jpg")

    await bot.send_photo(
        chat_id=callback.from_user.id,
        photo=image,
        reply_markup=menu.get_menu()
    )

    await message.delete()
