from src.guides.viz_posts import VIZ_SEVENTEENTH_POST_NUMBER
from src.guides.viz_seventeenth_post import DEFAULT_VIZ_SEVENTEENTH_POST
from src.guides.viz_seventeenth_post import OLD_FACTORY_CANTEEN_URL
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_viz_seventeenth_post_is_available_and_formats_address_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_SEVENTEENTH_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_SEVENTEENTH_POST
    assert OLD_FACTORY_CANTEEN_URL.replace("&", "&amp;") in formatted_text
    assert ">Кирова, 28</a>" in formatted_text
