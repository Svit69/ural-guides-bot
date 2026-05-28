from aiogram.fsm.state import State, StatesGroup


class FeedbackStates(StatesGroup):
    waiting_for_feedback = State()
    waiting_for_confirmation = State()
