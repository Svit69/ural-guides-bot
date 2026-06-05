from src.admin.callbacks import AdminCallbackData
from src.admin.keyboards import AdminKeyboardFactory


def test_builds_admin_guide_selection_keyboard() -> None:
    keyboard = AdminKeyboardFactory().build_guide_selection_keyboard()

    assert keyboard.inline_keyboard[0][0].text == "ВИЗ"
    assert keyboard.inline_keyboard[0][0].callback_data == "admin:guide:viz"
    assert keyboard.inline_keyboard[1][0].text == "Большой Конный п-ов"
    assert keyboard.inline_keyboard[-1][0].text == "Отменить"


def test_builds_admin_main_keyboard_with_viz_buyers_button() -> None:
    keyboard = AdminKeyboardFactory().build_main_keyboard()

    assert keyboard.inline_keyboard[1][0].text == "Купили гайд по ВИЗу"
    assert keyboard.inline_keyboard[1][0].callback_data == AdminCallbackData.VIZ_BUYERS


def test_builds_big_konny_post_selection_keyboard() -> None:
    keyboard = AdminKeyboardFactory().build_post_selection_keyboard(
        AdminCallbackData.GUIDE_BIG_KONNY
    )

    assert keyboard.inline_keyboard[0][0].text == "1. Приветствие"
    assert keyboard.inline_keyboard[0][0].callback_data == "admin:post:1"
    assert keyboard.inline_keyboard[-2][0].text == "12. Финальный пост"


def test_builds_viz_post_selection_keyboard() -> None:
    keyboard = AdminKeyboardFactory().build_post_selection_keyboard(
        AdminCallbackData.GUIDE_VIZ
    )

    assert keyboard.inline_keyboard[0][0].text == "101. Первый пост"
    assert keyboard.inline_keyboard[1][0].text == "102. Дворец молодёжи"
    assert keyboard.inline_keyboard[-1][0].callback_data == AdminCallbackData.CANCEL


def test_parses_admin_selection_callbacks() -> None:
    assert AdminCallbackData.parse_guide_id("admin:guide:viz") == "viz"
    assert AdminCallbackData.parse_guide_id("admin:guide:unknown") is None
    assert AdminCallbackData.parse_post_number("admin:post:12") == 12
    assert AdminCallbackData.parse_post_number("admin:users") is None
