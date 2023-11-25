from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext

from utils.get_photo_message import get_photo_with_id
from utils.get_last_block import get_last_block

from keyboards.inline import menu

back_button_router = Router()


#  Обработчик кнопки Назад🔙
@back_button_router.callback_query(F.data.contains("back_"))
async def back_button_(callback: types.CallbackQuery, bot: Bot, state: FSMContext):

    await callback.message.delete()

    message = await bot.send_photo(
        chat_id=callback.from_user.id,
        photo=types.FSInputFile('photo/load.jpg')
    )

    #  Получаем данные из state
    state_data = await state.get_data()

    caption = state_data["block_text"]  # Описание к фото
    photo_id = state_data["photo_id"]  # id фотографии
    image = await get_photo_with_id(photo_id=photo_id)
    last_block_id = callback.data.split("_")[-1]
    if last_block_id == "5":

        input_image = types.BufferedInputFile(image, "photo.jpg")
        keyboard = await menu.get_shops(last_block=last_block_id)
        await bot.send_photo(
            chat_id=callback.from_user.id,
            photo=input_image,
            caption=caption,
            reply_markup=keyboard
        )
        await state.clear()
        await message.delete()
        return

    # Получаем информацию о следующем блоке
    last_block_info = await get_last_block(shop_id=last_block_id)

    new_last_block = last_block_info[0]
    new_photo_id = last_block_info[1]
    block_text = last_block_info[2]

    input_image = types.BufferedInputFile(image, "photo.jpg")

    keyboard = await menu.get_child(last_block=last_block_id, back_block=new_last_block)
    await bot.send_photo(
        chat_id=callback.from_user.id,
        photo=input_image,
        caption=caption,
        reply_markup=keyboard
    )
    await state.update_data(
        back_button_id=new_last_block,
        photo_id=new_photo_id,
        block_text=block_text
    )

    await message.delete()
