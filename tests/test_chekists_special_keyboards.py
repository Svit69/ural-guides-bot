from src.guides.chekists_keyboards import ChekistsKeyboardFactory


def test_builds_find_all_idols_keyboard() -> None:
    keyboard = ChekistsKeyboardFactory().build_find_all_idols_keyboard()
    button = keyboard.inline_keyboard[0][0]

    assert button.text == "хочу найти всех"
    assert button.callback_data == "guide:chekists:idols:find_all"


def test_builds_second_idol_next_keyboard() -> None:
    keyboard = ChekistsKeyboardFactory().build_second_idol_next_keyboard()
    button = keyboard.inline_keyboard[0][0]

    assert button.text == "2/7 идем дальше"
    assert button.callback_data == "guide:chekists:next:15"


def test_builds_third_idol_next_keyboard() -> None:
    keyboard = ChekistsKeyboardFactory().build_third_idol_next_keyboard()
    button = keyboard.inline_keyboard[0][0]

    assert button.text == "3/7 идем дальше"
    assert button.callback_data == "guide:chekists:next:17"


def test_builds_fourth_idol_next_keyboard() -> None:
    keyboard = ChekistsKeyboardFactory().build_fourth_idol_next_keyboard()
    button = keyboard.inline_keyboard[0][0]

    assert button.text == "4/7 идем дальше"
    assert button.callback_data == "guide:chekists:next:18"


def test_builds_fifth_idol_next_keyboard() -> None:
    keyboard = ChekistsKeyboardFactory().build_idol_next_keyboard(5, "guide:chekists:next:19")
    button = keyboard.inline_keyboard[0][0]

    assert button.text == "5/7 идем дальше"
    assert button.callback_data == "guide:chekists:next:19"


def test_builds_sixth_idol_next_keyboard() -> None:
    keyboard = ChekistsKeyboardFactory().build_idol_next_keyboard(6, "guide:chekists:next")
    button = keyboard.inline_keyboard[0][0]

    assert button.text == "6/7 идем дальше"
    assert button.callback_data == "guide:chekists:next"
