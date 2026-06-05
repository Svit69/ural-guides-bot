from src.guides.viz_posts import VIZ_THIRTEENTH_POST_NUMBER
from src.guides.viz_thirteenth_post import CHURCH_REFECTORY_URL
from src.guides.viz_thirteenth_post import DEFAULT_VIZ_THIRTEENTH_POST
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_viz_thirteenth_post_is_available_and_formats_address_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_THIRTEENTH_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_THIRTEENTH_POST
    assert CHURCH_REFECTORY_URL.replace("&", "&amp;") in formatted_text
    assert ">Кирова, 65/2</a>" in formatted_text
