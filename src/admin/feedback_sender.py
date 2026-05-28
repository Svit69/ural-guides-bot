from aiogram.types import Message

from src.admin.feedback_presenter import FeedbackPresenter


class AdminFeedbackSender:
    def __init__(self) -> None:
        self.__presenter = FeedbackPresenter()

    async def send_feedback(self, message: Message, feedback: dict[str, object]) -> None:
        text = self.__presenter.build_feedback_text(feedback)
        media_type = feedback.get("media_type")
        file_id = feedback.get("file_id")
        if media_type == "photo" and file_id:
            await message.answer_photo(str(file_id), caption=text)
        elif media_type == "video" and file_id:
            await message.answer_video(str(file_id), caption=text)
        else:
            await message.answer(text)
