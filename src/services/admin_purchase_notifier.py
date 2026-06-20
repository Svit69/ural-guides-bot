from aiogram import Bot
from aiogram.exceptions import TelegramAPIError
from aiogram.types import User
import logging

from src.admin.purchase_notification_text import PurchaseNotificationText
from src.repositories.admin_repository import AdminRepository


class AdminPurchaseNotifier:
    def __init__(self, admins: AdminRepository) -> None:
        self.__admins = admins
        self.__text = PurchaseNotificationText()

    async def notify_purchase(self, bot: Bot, user: User, guide_name: str) -> None:
        text = self.__text.build_text(user, guide_name)
        for admin_id in self.__admins.get_all_admin_ids():
            try:
                await bot.send_message(admin_id, text)
            except TelegramAPIError:
                logging.exception("Failed to send purchase notification")
