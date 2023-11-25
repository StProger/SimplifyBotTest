from aiogram import Router, types, Bot, F
from aiogram.fsm.context import FSMContext

from keyboards.inline import menu

from utils.get_photo_message import get_photo
from utils.get_caption import get_caption
from utils.get_last_block import get_last_block


shop_router = Router()


# Обработчик кнопки Магазин🎮
@shop_router.callback_query(F.data == "id_5")
async def shop(callback: types.CallbackQuery, bot: Bot):

    await callback.message.delete()

    message = await bot.send_photo(
        chat_id=callback.from_user.id,
        photo=types.FSInputFile('photo/load.jpg')
    )

    keyboard = await menu.get_shops(callback.data.split("_")[1])

    image = await get_photo(last_block_id=callback.data.split("_")[1])

    caption = await get_caption(shop_id=callback.data.split("_")[-1])

    input_image = types.BufferedInputFile(image, "shop_photo.jpg")
    await bot.send_photo(chat_id=callback.from_user.id,
                         photo=input_image,
                         caption=caption,
                         reply_markup=keyboard)

    await message.delete()


# Обработчик остальных кнопок после Магазин🎮
@shop_router.callback_query(F.data.contains("shop_id_"))
async def choose_point(callback: types.CallbackQuery, state: FSMContext, bot: Bot):

    await callback.message.delete()

    message = await bot.send_photo(
        chat_id=callback.from_user.id,
        photo=types.FSInputFile('photo/load.jpg')
    )

    shop_id = callback.data.split("_")[-1]

    last_block_info = await get_last_block(shop_id=shop_id)  # Получаем информацию о предыдущем блоке

    last_block = last_block_info[0]
    photo_id = last_block_info[1]
    block_text = last_block_info[2]

    # Обновляем данные
    await state.update_data(
        back_button_id=last_block,
        photo_id=photo_id,
        block_text=block_text
    )

    caption = await get_caption(shop_id=shop_id)
    image = await get_photo(last_block_id=shop_id)

    keyboard = await menu.get_child(last_block=shop_id, back_block=last_block)

    input_image = types.BufferedInputFile(image, "shop_photo.jpg")

    await bot.send_photo(
        chat_id=callback.from_user.id,
        photo=input_image,
        caption=caption,
        reply_markup=keyboard
    )

    await message.delete()
