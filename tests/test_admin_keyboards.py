from src.admin.callbacks import AdminCallbackData
from src.admin.keyboards import AdminKeyboardFactory


def test_builds_readable_post_selection_keyboard() -> None:
    keyboard = AdminKeyboardFactory().build_post_selection_keyboard()
    first_button = keyboard.inline_keyboard[0][0]
    last_button = keyboard.inline_keyboard[-1][0]

    assert first_button.text == "1. Приветствие"
    assert first_button.callback_data == "admin:post:1"
    assert last_button.text == "Отменить"
    assert last_button.callback_data == AdminCallbackData.CANCEL


def test_parses_selected_post_number() -> None:
    assert AdminCallbackData.parse_post_number("admin:post:12") == 12
    assert AdminCallbackData.parse_post_number("admin:users") is None
