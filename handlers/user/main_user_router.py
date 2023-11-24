from aiogram import Router

from .start import start_router
from .shop import shop_router
from .go_menu import go_home_router


main_user_router = Router()
main_user_router.include_routers(
    start_router,
    shop_router,
    go_home_router
)