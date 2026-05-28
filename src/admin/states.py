from aiogram.fsm.state import State, StatesGroup


class AddAdminStates(StatesGroup):
    waiting_for_telegram_id = State()


class EditContentStates(StatesGroup):
    waiting_for_post_number = State()
    waiting_for_replacement_text = State()
    waiting_for_photo = State()
