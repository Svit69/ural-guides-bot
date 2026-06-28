from src.guides.chekists_keyboards import ChekistsKeyboardFactory


def test_builds_final_idol_next_keyboard() -> None:
    keyboard = ChekistsKeyboardFactory().build_idol_next_keyboard(7, "guide:chekists:next")
    button = keyboard.inline_keyboard[0][0]

    assert button.text == "нашли всех, идем дальше!"
    assert button.callback_data == "guide:chekists:next"
