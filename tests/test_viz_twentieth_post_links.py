from src.guides.viz_post_numbers import VIZ_TWENTIETH_POST_NUMBER
from src.guides.viz_twentieth_post import DEFAULT_VIZ_TWENTIETH_POST, VIZ_POND_URL
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_viz_twentieth_post_is_available_and_formats_map_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_TWENTIETH_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_TWENTIETH_POST
    assert VIZ_POND_URL.replace("&", "&amp;") in formatted_text
    assert ">Точка на карте</a>" in formatted_text
