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


async def get_shops(last_block: str):
    """
    Функция для получения списка кнопок после нажатия на кнопку "Магазин🎮"
    :param last_block:
    :return:
    """

    builder = InlineKeyboardBuilder()

    url = f"https://api.simplify-bots.com/items/routes_level_up_bot?filter[last_block][_eq]={last_block}&sort=row,column"

    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}'
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=url) as response:

            response_data = await response.json()

    dict_places = {}

    for data in response_data["data"]:

        if data["status"] and data["row"] is not None:

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


async def get_child(last_block, back_block):
    """
    Функция для создания клавиатур после кнопки Магазин🎮
    :param last_block:
    :param back_block:
    :return:
    """

    builder = InlineKeyboardBuilder()

    # URL для запроса с сортировкой по строкам и столбцам
    url = f"https://api.simplify-bots.com/items/routes_level_up_bot?filter[last_block][_eq]={last_block}&sort=row,column"

    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}'
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=url) as response:
            response_data = await response.json()

    dict_places = {}

    for data in response_data["data"]:

        if data["status"] and data["row"] is not None:

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
        elif data["status"] and data["row"] is None and data["button_text"] != "{{null}}":
            builder.row(
                types.InlineKeyboardButton(
                    text=data["button_text"], callback_data=f"shop_id_{data['id']}"
                )
            )

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
            text="Корзина🛒", callback_data="trasher"
        )
    )

    builder.row(
        types.InlineKeyboardButton(
            text="Назад🔙", callback_data=f"back_{back_block}"
        )
    )

    builder.add(
        types.InlineKeyboardButton(
            text="Меню🏠", callback_data="go_menu"
        )
    )
    return builder.as_markup()
