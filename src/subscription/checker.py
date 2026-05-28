from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError


class ChannelSubscriptionChecker:
    def __init__(self, channel_username: str) -> None:
        self.__channel_username = channel_username

    async def has_active_subscription(self, bot: Bot, user_id: int) -> bool:
        try:
            member = await bot.get_chat_member(self.__channel_username, user_id)
        except (TelegramBadRequest, TelegramForbiddenError):
            raise
        if member.status in {"creator", "administrator", "member"}:
            return True
        return bool(getattr(member, "is_member", False))
