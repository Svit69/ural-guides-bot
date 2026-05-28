from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.admin.keyboards import AdminKeyboardFactory
from src.admin.states import EditContentStates


class PhotoQuestionSender:
    def __init__(self) -> None:
        self.__keyboard_factory = AdminKeyboardFactory()

    async def ask_photo_question(self, message: Message, state: FSMContext) -> None:
        await state.set_state(EditContentStates.waiting_for_photo)
        await message.answer(
            "Добавить фотографию?",
            reply_markup=self.__keyboard_factory.build_photo_decision_keyboard(),
        )
