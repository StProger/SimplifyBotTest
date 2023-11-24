import requests

url = "https://api.simplify-bots.com/items/routes_level_up_bot?filter[last_block][_eq]=5"
payload = {}
headers = {
    'Authorization': 'Bearer UokPEWhb7Gjf2hrqjRv_FlHOzWPSViPG'
}

response = requests.request("GET", url, headers=headers, data=payload).json()

for data in response["data"]:
    if data["callback_data_special"] == None:
        print(data)


