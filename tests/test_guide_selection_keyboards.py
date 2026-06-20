from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory


def test_builds_guide_selection_keyboard() -> None:
    keyboard = GuideKeyboardFactory().build_guide_selection_keyboard("500.00", False, "700.00")
    viz_button = keyboard.inline_keyboard[0][0]
    city_button = keyboard.inline_keyboard[1][0]
    big_konny_button = keyboard.inline_keyboard[2][0]

    assert viz_button.text == "ВИЗ 500 ₽ 💳"
    assert viz_button.callback_data == GuideCallbackData.SELECT_VIZ
    assert city_button.text == "Прогулка по Екатеринбургу 700 ₽ 💳"
    assert city_button.callback_data == GuideCallbackData.SELECT_CITY_WALK
    assert big_konny_button.text == "Большой Конный п-ов"
    assert big_konny_button.callback_data == GuideCallbackData.SELECT_BIG_KONNY


def test_builds_paid_user_guide_selection_keyboard() -> None:
    keyboard = GuideKeyboardFactory().build_guide_selection_keyboard("500.00", True)
    viz_button = keyboard.inline_keyboard[0][0]

    assert viz_button.text == "ВИЗ"
    assert viz_button.callback_data == GuideCallbackData.SELECT_VIZ


def test_builds_viz_next_keyboard() -> None:
    button = GuideKeyboardFactory().build_viz_next_keyboard().inline_keyboard[0][0]

    assert button.text == "идем дальше"
    assert button.callback_data == GuideCallbackData.VIZ_NEXT


def test_builds_viz_next_keyboard_after_second_post() -> None:
    keyboard = GuideKeyboardFactory().build_viz_next_keyboard(
        GuideCallbackData.VIZ_NEXT_AFTER_SECOND
    )
    assert keyboard.inline_keyboard[0][0].callback_data == "guide:viz:next:2"


def test_builds_viz_next_keyboard_after_third_post() -> None:
    keyboard = GuideKeyboardFactory().build_viz_next_keyboard(
        GuideCallbackData.VIZ_NEXT_AFTER_THIRD
    )
    assert keyboard.inline_keyboard[0][0].callback_data == "guide:viz:next:3"
