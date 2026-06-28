from src.guides.chekists_keyboards import ChekistsKeyboardFactory


def test_final_idol_button_can_continue_to_next_post() -> None:
    keyboard = ChekistsKeyboardFactory().build_idol_next_keyboard(7, "guide:chekists:next:29")
    button = keyboard.inline_keyboard[0][0]

    assert button.text == "нашли всех, идем дальше!"
    assert button.callback_data == "guide:chekists:next:29"
