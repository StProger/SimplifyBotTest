from aiogram import Router, types, Bot, F
from aiogram.fsm.context import FSMContext

from keyboards.inline import menu

from utils.get_photo_message import get_photo

# Роутер для кнопки Магазин
shop_router = Router()


@shop_router.callback_query(F.data == "id_5")
async def shop(callback: types.CallbackQuery, state: FSMContext, bot: Bot):

    keyboard = await menu.get_shops(callback.data.split("_")[1])

    image = await get_photo(last_block_id=callback.data.split("_")[1])

    input_image = types.BufferedInputFile(image, "shop_photo.jpg")
    await bot.send_photo(chat_id=callback.from_user.id,
                         photo=input_image,
                         reply_markup=keyboard)

    await callback.message.delete()
