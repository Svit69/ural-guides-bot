from aiogram import Bot

from src.repositories.admin_repository import AdminRepository


class FeedbackAdminNotifier:
    def __init__(self, admin_repository: AdminRepository) -> None:
        self.__admin_repository = admin_repository

    async def notify_admins(self, bot: Bot, payload: dict[str, object]) -> None:
        for admin_id in self.__admin_repository.get_all_admin_ids():
            await self.__send_feedback_to_admin(bot, admin_id, payload)

    async def __send_feedback_to_admin(self, bot: Bot, admin_id: int, payload) -> None:
        text = self.__build_admin_text(payload)
        media = payload.get("media")
        if media is None:
            await bot.send_message(admin_id, text)
        elif media["media_type"] == "photo":
            await bot.send_photo(admin_id, media["file_id"], caption=text)
        else:
            await bot.send_video(admin_id, media["file_id"], caption=text)

    def __build_admin_text(self, payload: dict[str, object]) -> str:
        return (
            "Новый отзыв\n"
            f"От: {payload.get('full_name')} ({payload.get('user_id')})\n\n"
            f"{payload.get('text') or 'Медиа без подписи'}"
        )
