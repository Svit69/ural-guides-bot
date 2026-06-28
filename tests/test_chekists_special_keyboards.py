from src.guides.chekists_keyboards import ChekistsKeyboardFactory


def test_builds_find_all_idols_keyboard() -> None:
    keyboard = ChekistsKeyboardFactory().build_find_all_idols_keyboard()
    button = keyboard.inline_keyboard[0][0]

    assert button.text == "хочу найти всех"
    assert button.callback_data == "guide:chekists:idols:find_all"
