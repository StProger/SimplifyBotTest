import aiohttp

from config import BEARER_TOKEN


async def get_photo(last_block_id: str) -> bytes:
    """
    Функция для получения фотографии сообщения
    :param last_block_id:
    :return:
    """

    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}'
    }

    # URL для получения id фотографии
    url_for_photo_id = f"https://api.simplify-bots.com/items/routes_level_up_bot?filter[id][_eq]={last_block_id}"

    async with aiohttp.ClientSession(headers=headers) as session:

        # Делаем запрос на получение данных об определённом id
        response = await session.get(url=url_for_photo_id)

        response_data = await response.json()

        photo_id = response_data["data"][0]["photo"]
        # URL для получения фотографии
        url_photo = f"https://api.simplify-bots.com/assets/{photo_id}"

        response_photo = await session.get(url=url_photo)

        image = await response_photo.read()

    return image
