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


def test_admin_can_select_chekists_posts_for_editing() -> None:
    keyboard = AdminKeyboardFactory().build_post_selection_keyboard(
        AdminCallbackData.GUIDE_CHEKISTS
    )
    assert keyboard.inline_keyboard[0][0].callback_data == "admin:post:301"
    assert keyboard.inline_keyboard[18][0].text == "319. Пятый идол"
    assert keyboard.inline_keyboard[19][0].text == "320. Жилой дом"
    assert keyboard.inline_keyboard[20][0].text == "321. Полянка"
    assert keyboard.inline_keyboard[21][0].text == "322. Жилые дома"
    assert keyboard.inline_keyboard[22][0].text == "323. Строчки из песни"
    assert keyboard.inline_keyboard[23][0].text == "324. Детский сад и ясли"
    assert keyboard.inline_keyboard[24][0].text == "325. Спортивная площадка"
    assert keyboard.inline_keyboard[25][0].text == "326. По пути до идола"
    assert keyboard.inline_keyboard[26][0].text == "327. Шестой идол"
    assert keyboard.inline_keyboard[27][0].text == "328. На будке"
    assert keyboard.inline_keyboard[28][0].text == "329. Седьмой идол"


def test_admin_visibility_keyboard_marks_hidden_chekists_guide() -> None:
    keyboard = GuideVisibilityKeyboardFactory().build_keyboard({GUIDE_CHEKISTS: False})
    assert keyboard.inline_keyboard[3][0].callback_data == "admin:toggle_guide:chekists"
