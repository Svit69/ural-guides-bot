from src.guides.viz_more_posts import DEFAULT_VIZ_FOURTH_POST, DEFAULT_VIZ_THIRD_POST
from src.guides.viz_posts import PARK_22_PART_CONGRESS_URL, SINARA_CENTER_URL
from src.guides.viz_posts import VIZ_FOURTH_POST_NUMBER, VIZ_THIRD_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_viz_third_post_is_available_and_formats_map_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_THIRD_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_THIRD_POST
    assert PARK_22_PART_CONGRESS_URL.replace("&", "&amp;") in formatted_text
    assert ">Точка на карте</a>" in formatted_text


def test_viz_fourth_post_is_available_and_formats_address_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_FOURTH_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_FOURTH_POST
    assert SINARA_CENTER_URL.replace("&", "&amp;") in formatted_text
    assert ">Верх-Исетский бульвар, 15/4</a>" in formatted_text
