from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory


def test_builds_chekists_finish_keyboard() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_finish_keyboard()
    button = keyboard.inline_keyboard[0][0]

    assert button.text == "завершить прогулку"
    assert button.callback_data == GuideCallbackData.FINISH_CHEKISTS
