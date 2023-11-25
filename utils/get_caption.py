import aiohttp

from config import BEARER_TOKEN


async def get_caption(shop_id):
    """
    Функция для получения описания фотографии
    :param shop_id:
    :return:
    """

    url = f"https://api.simplify-bots.com/items/routes_level_up_bot?filter[id][_eq]={shop_id}"

    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}'
    }

    async with aiohttp.ClientSession(headers=headers) as session:

        response = await session.get(url=url)
        response_data = await response.json()

    return response_data["data"][0]["block_text"]
