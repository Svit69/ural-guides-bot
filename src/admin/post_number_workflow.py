from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.admin.keyboards import AdminKeyboardFactory
from src.admin.post_number_prompts import TEXT_DECISION_PROMPT
from src.admin.post_selection import PostSelectionCatalog


class AdminPostNumberWorkflow:
    def __init__(self) -> None:
        self.__keyboard_factory = AdminKeyboardFactory()
        self.__post_catalog = PostSelectionCatalog()

    async def ask_text_decision(
        self, message: Message, state: FSMContext, post_number: int
    ) -> None:
        await state.update_data(post_number=post_number)
        await message.answer(
            TEXT_DECISION_PROMPT,
            reply_markup=self.__keyboard_factory.build_text_decision_keyboard(),
        )

    async def is_selected_guide_post(self, state: FSMContext, post_number: int) -> bool:
        guide_id = (await state.get_data()).get("guide_id", "")
        return self.__post_catalog.contains_post(str(guide_id), post_number)

    def parse_post_number(self, raw_value: str | None) -> int | None:
        value = int(raw_value.strip()) if raw_value and raw_value.strip().isdigit() else 0
        return value if value > 0 else None
