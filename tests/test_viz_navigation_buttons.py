import pytest

from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory


@pytest.mark.parametrize(
    ("callback_data", "expected_data"),
    [
        (GuideCallbackData.VIZ_NEXT_AFTER_FOURTH, "guide:viz:next:4"),
        (GuideCallbackData.VIZ_NEXT_AFTER_FIFTH, "guide:viz:next:5"),
        (GuideCallbackData.VIZ_NEXT_AFTER_SIXTH, "guide:viz:next:6"),
        (GuideCallbackData.VIZ_NEXT_AFTER_SEVENTH, "guide:viz:next:7"),
        (GuideCallbackData.VIZ_NEXT_AFTER_EIGHTH, "guide:viz:next:8"),
        (GuideCallbackData.VIZ_NEXT_AFTER_NINTH, "guide:viz:next:9"),
        (GuideCallbackData.VIZ_NEXT_AFTER_TENTH, "guide:viz:next:10"),
        (GuideCallbackData.VIZ_NEXT_AFTER_ELEVENTH, "guide:viz:next:11"),
        (GuideCallbackData.VIZ_NEXT_AFTER_TWELFTH, "guide:viz:next:12"),
        (GuideCallbackData.VIZ_NEXT_AFTER_THIRTEENTH, "guide:viz:next:13"),
        (GuideCallbackData.VIZ_NEXT_AFTER_FOURTEENTH, "guide:viz:next:14"),
        (GuideCallbackData.VIZ_NEXT_AFTER_FIFTEENTH, "guide:viz:next:15"),
        (GuideCallbackData.VIZ_NEXT_AFTER_SIXTEENTH, "guide:viz:next:16"),
        (GuideCallbackData.VIZ_NEXT_AFTER_SEVENTEENTH, "guide:viz:next:17"),
        (GuideCallbackData.VIZ_NEXT_AFTER_EIGHTEENTH, "guide:viz:next:18"),
        (GuideCallbackData.VIZ_NEXT_AFTER_NINETEENTH, "guide:viz:next:19"),
        (GuideCallbackData.VIZ_NEXT_AFTER_TWENTIETH, "guide:viz:next:20"),
    ],
)
def test_builds_viz_next_keyboard(callback_data: str, expected_data: str) -> None:
    keyboard = GuideKeyboardFactory().build_viz_next_keyboard(callback_data)

    assert keyboard.inline_keyboard[0][0].callback_data == expected_data


def test_builds_viz_baby_head_keyboard() -> None:
    keyboard = GuideKeyboardFactory().build_viz_baby_head_keyboard()
    button = keyboard.inline_keyboard[0][0]

    assert button.text == "почему на пляже голова младенца?"
    assert button.callback_data == "guide:viz:next:20"
