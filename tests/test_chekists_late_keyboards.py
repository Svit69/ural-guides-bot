from src.guides.keyboards import GuideKeyboardFactory


def test_builds_chekists_next_keyboard_after_sixteenth_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard("guide:chekists:next:16")

    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:16"


def test_builds_chekists_next_keyboard_after_nineteenth_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard("guide:chekists:next:19")

    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:19"


def test_builds_chekists_next_keyboard_after_twentieth_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard("guide:chekists:next:20")

    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:20"


def test_builds_chekists_next_keyboard_after_twenty_first_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard("guide:chekists:next:21")

    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:21"


def test_builds_chekists_next_keyboard_after_twenty_second_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard("guide:chekists:next:22")

    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:22"


def test_builds_chekists_next_keyboard_after_twenty_third_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard("guide:chekists:next:23")

    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:23"
