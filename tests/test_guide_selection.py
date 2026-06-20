from src.guides.viz_posts import DEFAULT_VIZ_FIRST_POST, DEFAULT_VIZ_SECOND_POST
from src.guides.viz_posts import PALACE_OF_YOUTH_URL
from src.guides.viz_posts import VIZ_FIRST_POST_NUMBER, VIZ_SECOND_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


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
