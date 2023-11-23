from aiogram import Router, types, Bot, F
from aiogram.fsm.context import FSMContext

import requests

from config import BEARER_TOKEN

from keyboards.inline import menu

# Роутер для кнопки Магазин
shop_router = Router()


@shop_router.callback_query(F.data=="id_5")
async def shop(callback: types.CallbackQuery, state: FSMContext, bot: Bot):

    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}'
    }

    url = f"https://api.simplify-bots.com/items/routes_level_up_bot?filter[id][_eq]={callback.data.split('_')[1]}"

    response = requests.get(url=url, headers=headers).json()
    print(response)

    photo_shop_id = response["data"][0]["photo"]

    url_photo = f"https://api.simplify-bots.com/assets/{photo_shop_id}"
    keyboard = await menu.get_shops(callback.data.split("_")[1])

    image = requests.get(url=url_photo, headers=headers).content

    input_image = types.BufferedInputFile(image, "shop_photo.jpg")
    await bot.send_photo(chat_id=callback.from_user.id,
                         photo=input_image,
                         reply_markup=keyboard)

    await callback.message.delete()