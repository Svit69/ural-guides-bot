from src.guides.viz_fourteenth_post import DEFAULT_VIZ_FOURTEENTH_POST
from src.guides.viz_fourteenth_post import USPENSKY_HOUSE_MUSEUM_URL
from src.guides.viz_posts import VIZ_FOURTEENTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_viz_fourteenth_post_is_available_and_formats_address_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_FOURTEENTH_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_FOURTEENTH_POST
    assert USPENSKY_HOUSE_MUSEUM_URL.replace("&", "&amp;") in formatted_text
    assert ">Синяева, 58</a>" in formatted_text
