from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.feedback.prompt_sender import FeedbackPromptSender
from src.messages.post_provider import PostProvider
from src.text_formatting.telegram_formatter import TelegramTextFormatter


class CityWalkGuideSender:
    def __init__(self, posts: PostProvider) -> None:
        self.__posts = posts
        self.__formatter = TelegramTextFormatter()
        self.__feedback_prompt = FeedbackPromptSender()

    async def send_guide(self, message: Message, post_number: int, state: FSMContext) -> None:
        post = self.__posts.get_post(post_number)
        text = self.__formatter.format_text(str(post["text"]))
        await message.answer(text, disable_web_page_preview=True)
        for item in list(post.get("media", [])):
            if item["media_type"] == "document":
                await message.answer_document(item["file_id"])
        await self.__feedback_prompt.send_feedback_prompt(message, state)
