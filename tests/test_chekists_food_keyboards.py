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


def test_builds_chekists_next_keyboard_after_eighth_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard("guide:chekists:next:8")
    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:8"


def test_builds_chekists_next_keyboard_after_ninth_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard("guide:chekists:next:9")
    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:9"


def test_builds_chekists_next_keyboard_after_tenth_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard("guide:chekists:next:10")
    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:10"


def test_builds_chekists_next_keyboard_after_twelfth_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard("guide:chekists:next:12")
    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:12"


def test_builds_chekists_next_keyboard_after_thirteenth_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard("guide:chekists:next:13")
    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:13"


def test_builds_chekists_next_keyboard_after_fourteenth_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard("guide:chekists:next:14")
    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:14"
