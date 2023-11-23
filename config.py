import os

from dotenv import load_dotenv


load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
BOT_TOKEN = os.getenv("BOT_TOKEN")