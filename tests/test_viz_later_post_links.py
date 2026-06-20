from src.guides.viz_eighth_post import DEFAULT_VIZ_EIGHTH_POST, STONE_HOUSE_URL
from src.guides.viz_ninth_post import DEFAULT_VIZ_NINTH_POST, WOODEN_HOUSE_URL
from src.guides.viz_tenth_post import DEFAULT_VIZ_TENTH_POST, VIZMUT_ART_OBJECT_URL
from src.guides.viz_posts import VIZ_EIGHTH_POST_NUMBER, VIZ_NINTH_POST_NUMBER
from src.guides.viz_posts import VIZ_TENTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_viz_eighth_post_is_available_and_formats_address_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_EIGHTH_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_EIGHTH_POST
    assert STONE_HOUSE_URL.replace("&", "&amp;") in formatted_text
    assert ">Кирова, 1</a>" in formatted_text


def test_viz_ninth_post_is_available_and_formats_address_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_NINTH_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_NINTH_POST
    assert WOODEN_HOUSE_URL.replace("&", "&amp;") in formatted_text
    assert ">Кирова, 3</a>" in formatted_text


def test_viz_tenth_post_is_available_and_formats_map_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_TENTH_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_TENTH_POST
    assert VIZMUT_ART_OBJECT_URL.replace("&", "&amp;") in formatted_text
    assert ">Точка на карте</a>" in formatted_text
