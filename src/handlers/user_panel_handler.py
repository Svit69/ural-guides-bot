from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.feedback.messages import FEEDBACK_CONTACT_PROMPT_TEXT
from src.feedback.prompt_sender import FeedbackPromptSender
from src.services.guide_list_sender import GuideListSender
from src.user_panel.messages import ALL_GUIDES_TEXT


class UserPanelHandler:
    def __init__(self, guide_list_sender: GuideListSender) -> None:
        self.__feedback_prompt_sender = FeedbackPromptSender()
        self.__guide_list_sender = guide_list_sender

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.message.register(self.__send_guides, F.text.casefold() == "все гайды")
        dispatcher.message.register(
            self.__start_feedback, F.text.casefold() == "обратная связь"
        )

    async def __send_guides(self, message: Message) -> None:
        await self.__guide_list_sender.send_guide_list(message, ALL_GUIDES_TEXT)

    async def __start_feedback(self, message: Message, state: FSMContext) -> None:
        await self.__feedback_prompt_sender.send_feedback_prompt(
            message, state, FEEDBACK_CONTACT_PROMPT_TEXT
        )
