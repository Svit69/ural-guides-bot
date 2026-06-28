from src.admin.callbacks import AdminCallbackData
from src.admin.keyboards import AdminKeyboardFactory
from src.admin.visibility_keyboard import GuideVisibilityKeyboardFactory
from src.guides.guide_ids import GUIDE_CHEKISTS


def test_admin_main_keyboard_has_guide_visibility_button() -> None:
    keyboard = AdminKeyboardFactory().build_main_keyboard()
    assert keyboard.inline_keyboard[5][0].callback_data == AdminCallbackData.GUIDE_VISIBILITY


def test_admin_guide_selection_contains_chekists_guide() -> None:
    keyboard = AdminKeyboardFactory().build_guide_selection_keyboard()
    assert keyboard.inline_keyboard[3][0].callback_data == "admin:guide:chekists"


def test_admin_can_select_chekists_start_post_for_editing() -> None:
    keyboard = AdminKeyboardFactory().build_post_selection_keyboard(
        AdminCallbackData.GUIDE_CHEKISTS
    )
    assert keyboard.inline_keyboard[0][0].callback_data == "admin:post:301"
    assert keyboard.inline_keyboard[9][0].text == "310. 5 арт-объектов"
    assert keyboard.inline_keyboard[10][0].text == "311. Шигирский идол"


def test_admin_visibility_keyboard_marks_hidden_chekists_guide() -> None:
    keyboard = GuideVisibilityKeyboardFactory().build_keyboard({GUIDE_CHEKISTS: False})
    assert keyboard.inline_keyboard[3][0].callback_data == "admin:toggle_guide:chekists"
