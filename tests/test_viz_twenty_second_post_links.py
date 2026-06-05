from src.guides.viz_post_numbers import VIZ_TWENTY_SECOND_POST_NUMBER
from src.guides.viz_twenty_second_post import DEFAULT_VIZ_TWENTY_SECOND_POST
from src.guides.viz_twenty_second_post import ZAVODSKAYA_MARKET_URL
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_viz_twenty_second_post_is_available_and_formats_map_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_TWENTY_SECOND_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_TWENTY_SECOND_POST
    assert ZAVODSKAYA_MARKET_URL.replace("&", "&amp;") in formatted_text
    assert ">Точка на карте</a>" in formatted_text
