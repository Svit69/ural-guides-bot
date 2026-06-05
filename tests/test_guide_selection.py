from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory
from src.guides.viz_posts import DEFAULT_VIZ_FIRST_POST, DEFAULT_VIZ_SECOND_POST
from src.guides.viz_posts import PALACE_OF_YOUTH_URL
from src.guides.viz_posts import VIZ_FIRST_POST_NUMBER, VIZ_SECOND_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_builds_guide_selection_keyboard() -> None:
    keyboard = GuideKeyboardFactory().build_guide_selection_keyboard("500.00")
    viz_button = keyboard.inline_keyboard[0][0]
    big_konny_button = keyboard.inline_keyboard[1][0]

    assert viz_button.text == "ВИЗ 500 ₽ 💳"
    assert viz_button.callback_data == GuideCallbackData.SELECT_VIZ
    assert big_konny_button.text == "Большой Конный п-ов"
    assert big_konny_button.callback_data == GuideCallbackData.SELECT_BIG_KONNY


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


def test_viz_first_post_keeps_placeholder_underscore_visible() -> None:
    formatted_text = TelegramTextFormatter().format_text(DEFAULT_VIZ_FIRST_POST)

    assert "_ часов" in formatted_text


def test_viz_first_post_is_available_from_default_catalog() -> None:
    assert DefaultPostCatalog().get_default_text(VIZ_FIRST_POST_NUMBER) == DEFAULT_VIZ_FIRST_POST


def test_viz_second_post_is_available_and_formats_address_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_SECOND_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_SECOND_POST
    assert PALACE_OF_YOUTH_URL.replace("&", "&amp;") in formatted_text
    assert ">Ленина, 1</a>" in formatted_text
