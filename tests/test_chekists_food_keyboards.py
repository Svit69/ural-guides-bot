from src.guides.keyboards import GuideKeyboardFactory


def test_builds_chekists_next_keyboard_after_fifth_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard("guide:chekists:next:5")

    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:5"


def test_builds_chekists_next_keyboard_after_sixth_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard("guide:chekists:next:6")

    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:6"


def test_builds_chekists_next_keyboard_after_seventh_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard("guide:chekists:next:7")

    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:7"
