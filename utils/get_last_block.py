import aiohttp

from config import BEARER_TOKEN


async def get_last_block(shop_id):

    # URL для получения блока родителя
    url = f"https://api.simplify-bots.com/items/routes_level_up_bot?filter[id][_eq]={shop_id}"

    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}'
    }

    async with aiohttp.ClientSession(headers=headers) as session:

        response_parent = await session.get(url=url)

        response_data = await response_parent.json()

        last_block_id = response_data["data"][0]["last_block"]

        # URL для получения id фото и block_text
        url_for_data = f"https://api.simplify-bots.com/items/routes_level_up_bot?filter[id][_eq]={last_block_id}"

        response = await session.get(url=url_for_data)

        response_info = await response.json()

    photo_id = response_info["data"][0]["photo"]
    block_text = response_info["data"][0]["block_text"]

    return last_block_id, photo_id, block_text



