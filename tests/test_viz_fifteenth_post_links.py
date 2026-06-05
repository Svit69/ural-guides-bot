from src.guides.viz_fifteenth_post import CULTURE_PALACE_URL
from src.guides.viz_fifteenth_post import DEFAULT_VIZ_FIFTEENTH_POST
from src.guides.viz_posts import VIZ_FIFTEENTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_viz_fifteenth_post_is_available_and_formats_address_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_FIFTEENTH_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_FIFTEENTH_POST
    assert CULTURE_PALACE_URL.replace("&", "&amp;") in formatted_text
    assert ">Заводская, 5</a>" in formatted_text
