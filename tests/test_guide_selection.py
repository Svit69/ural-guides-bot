from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory
from src.guides.viz_posts import DEFAULT_VIZ_FIRST_POST
from src.guides.viz_posts import VIZ_FIRST_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_builds_guide_selection_keyboard() -> None:
    keyboard = GuideKeyboardFactory().build_guide_selection_keyboard()
    viz_button = keyboard.inline_keyboard[0][0]
    big_konny_button = keyboard.inline_keyboard[1][0]

    assert viz_button.text == "ВИЗ 💳"
    assert viz_button.callback_data == GuideCallbackData.SELECT_VIZ
    assert big_konny_button.text == "Большой Конный п-ов"
    assert big_konny_button.callback_data == GuideCallbackData.SELECT_BIG_KONNY


def test_builds_viz_next_keyboard() -> None:
    button = GuideKeyboardFactory().build_viz_next_keyboard().inline_keyboard[0][0]

    assert button.text == "идем дальше"
    assert button.callback_data == GuideCallbackData.VIZ_NEXT


def test_viz_first_post_keeps_placeholder_underscore_visible() -> None:
    formatted_text = TelegramTextFormatter().format_text(DEFAULT_VIZ_FIRST_POST)

    assert "_ часов" in formatted_text


def test_viz_first_post_is_available_from_default_catalog() -> None:
    assert DefaultPostCatalog().get_default_text(VIZ_FIRST_POST_NUMBER) == DEFAULT_VIZ_FIRST_POST
