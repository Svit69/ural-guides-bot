from src.admin.callbacks import AdminCallbackData
from src.admin.keyboards import AdminKeyboardFactory
from src.admin.visibility_keyboard import GuideVisibilityKeyboardFactory
from src.guides.guide_ids import GUIDE_CHEKISTS


def test_admin_main_keyboard_has_guide_visibility_button() -> None:
    keyboard = AdminKeyboardFactory().build_main_keyboard()

    assert keyboard.inline_keyboard[5][0].callback_data == AdminCallbackData.GUIDE_VISIBILITY


def test_admin_guide_selection_contains_chekists_guide() -> None:
    keyboard = AdminKeyboardFactory().build_guide_selection_keyboard()

    assert keyboard.inline_keyboard[3][0].text == "Городок чекистов"
    assert keyboard.inline_keyboard[3][0].callback_data == "admin:guide:chekists"


def test_admin_can_select_chekists_start_post_for_editing() -> None:
    keyboard = AdminKeyboardFactory().build_post_selection_keyboard(
        AdminCallbackData.GUIDE_CHEKISTS
    )

    assert keyboard.inline_keyboard[0][0].text == "301. Старт"
    assert keyboard.inline_keyboard[0][0].callback_data == "admin:post:301"
    assert keyboard.inline_keyboard[1][0].text == "302. Немного вводных"
    assert keyboard.inline_keyboard[2][0].text == "303. Гостиница «Исеть»"
    assert keyboard.inline_keyboard[3][0].text == "304. Жилые корпуса"
    assert keyboard.inline_keyboard[4][0].text == "305. Граффити «Слово пацана»"


def test_admin_visibility_keyboard_marks_hidden_chekists_guide() -> None:
    keyboard = GuideVisibilityKeyboardFactory().build_keyboard({GUIDE_CHEKISTS: False})
    button = keyboard.inline_keyboard[3][0]

    assert button.text == "Городок чекистов: скрыт"
    assert button.callback_data == "admin:toggle_guide:chekists"
