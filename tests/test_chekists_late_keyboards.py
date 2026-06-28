from src.guides.keyboards import GuideKeyboardFactory


def test_builds_chekists_next_keyboard_after_sixteenth_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard("guide:chekists:next:16")

    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:16"
