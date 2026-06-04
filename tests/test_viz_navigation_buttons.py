from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory


def test_builds_viz_next_keyboard_after_fourth_post() -> None:
    keyboard = GuideKeyboardFactory().build_viz_next_keyboard(
        GuideCallbackData.VIZ_NEXT_AFTER_FOURTH
    )

    assert keyboard.inline_keyboard[0][0].callback_data == "guide:viz:next:4"


def test_builds_viz_next_keyboard_after_fifth_post() -> None:
    keyboard = GuideKeyboardFactory().build_viz_next_keyboard(
        GuideCallbackData.VIZ_NEXT_AFTER_FIFTH
    )

    assert keyboard.inline_keyboard[0][0].callback_data == "guide:viz:next:5"


def test_builds_viz_next_keyboard_after_sixth_post() -> None:
    keyboard = GuideKeyboardFactory().build_viz_next_keyboard(
        GuideCallbackData.VIZ_NEXT_AFTER_SIXTH
    )

    assert keyboard.inline_keyboard[0][0].callback_data == "guide:viz:next:6"


def test_builds_viz_next_keyboard_after_seventh_post() -> None:
    keyboard = GuideKeyboardFactory().build_viz_next_keyboard(
        GuideCallbackData.VIZ_NEXT_AFTER_SEVENTH
    )

    assert keyboard.inline_keyboard[0][0].callback_data == "guide:viz:next:7"
