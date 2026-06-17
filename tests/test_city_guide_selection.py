from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory


def test_builds_paid_city_guide_selection_keyboard() -> None:
    keyboard = GuideKeyboardFactory().build_guide_selection_keyboard(
        "500.00", False, "700.00", True
    )
    city_button = keyboard.inline_keyboard[1][0]

    assert city_button.text == "Прогулка по Екатеринбургу"
    assert city_button.callback_data == GuideCallbackData.SELECT_CITY_WALK
