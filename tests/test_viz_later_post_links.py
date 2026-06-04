from src.guides.viz_eighth_post import DEFAULT_VIZ_EIGHTH_POST, STONE_HOUSE_URL
from src.guides.viz_posts import VIZ_EIGHTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_viz_eighth_post_is_available_and_formats_address_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_EIGHTH_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_EIGHTH_POST
    assert STONE_HOUSE_URL.replace("&", "&amp;") in formatted_text
    assert ">Кирова, 1</a>" in formatted_text
