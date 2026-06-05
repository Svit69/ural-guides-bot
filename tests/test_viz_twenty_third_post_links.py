from src.guides.viz_post_numbers import VIZ_TWENTY_THIRD_POST_NUMBER
from src.guides.viz_twenty_third_post import CHINESE_WALL_HOUSE_URL
from src.guides.viz_twenty_third_post import DEFAULT_VIZ_TWENTY_THIRD_POST
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_viz_twenty_third_post_is_available_and_formats_address_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_TWENTY_THIRD_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_TWENTY_THIRD_POST
    assert CHINESE_WALL_HOUSE_URL.replace("&", "&amp;") in formatted_text
    assert ">Татищева, 77</a>" in formatted_text
