from aiogram.types import Message

from src.feedback.messages import (
    FEEDBACK_LATER_TEXT,
    FEEDBACK_SENT_TEXT,
    GUIDE_LIST_AFTER_FEEDBACK_TEXT,
)
from src.services.guide_list_sender import GuideListSender


class FeedbackCompletionSender:
    def __init__(self, guide_list_sender: GuideListSender) -> None:
        self.__guide_list_sender = guide_list_sender

    async def send_success(self, message: Message, user_id: int) -> None:
        await message.answer(FEEDBACK_SENT_TEXT)
        await self.__send_guides(message, user_id)

    async def send_later(self, message: Message, user_id: int) -> None:
        await message.answer(FEEDBACK_LATER_TEXT)
        await self.__send_guides(message, user_id)

    async def __send_guides(self, message: Message, user_id: int) -> None:
        await self.__guide_list_sender.send_guide_list(
            message, GUIDE_LIST_AFTER_FEEDBACK_TEXT, user_id
        )
