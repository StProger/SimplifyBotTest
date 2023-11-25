from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

import aiohttp

from config import BEARER_TOKEN


# Inline-клавиатура с кнопкой Магазин
def get_menu():

    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text="Магазин🎮", callback_data="id_5"
        )
    )

    return builder.as_markup()


async def get_shops(last_block):
    """
    Функция для получения списка кнопок после нажатия на кнопку "Магазин🎮"
    :param last_block:
    :return:
    """

    builder = InlineKeyboardBuilder()

    url = f"https://api.simplify-bots.com/items/routes_level_up_bot?filter[last_block][_eq]={last_block}&sort=row,column"
    # filter[row][_neq]=None&filter[column][_neq]=None

    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}'
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=url) as response:

            response_data = await response.json()

    dict_places = {}

    for data in response_data["data"]:

        if data["status"] and data["row"] is not None:
            print(data["button_text"])

            if dict_places.get(data["row"], None) is None:

                dict_places[data["row"]] = []
                dict_places[data["row"]].append(
                    types.InlineKeyboardButton(
                        text=data["button_text"], callback_data=f"shop_id_{data['id']}"
                    )
                )
            else:
                dict_places[data["row"]].append(
                    types.InlineKeyboardButton(
                        text=data["button_text"], callback_data=f"shop_id_{data['id']}"
                    )
                )
    print(dict_places)

    for row in dict_places.keys():
        list_buttons = dict_places[row]
        if len(list_buttons) == 1:
            builder.row(list_buttons[0])
        else:
            builder.row(list_buttons[0])
            for button in list_buttons[1:]:
                builder.add(button)
    builder.row(
        types.InlineKeyboardButton(
            text="Меню🏠", callback_data="go_menu"
        )
    )
    return builder.as_markup()