from src.guides.viz_eleventh_post import DEFAULT_VIZ_ELEVENTH_POST, SARAFANOV_HOUSE_URL
from src.guides.viz_twelfth_post import DEFAULT_VIZ_TWELFTH_POST, ASSUMPTION_CHURCH_URL
from src.guides.viz_posts import VIZ_ELEVENTH_POST_NUMBER, VIZ_TWELFTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_viz_eleventh_post_is_available_and_formats_address_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_ELEVENTH_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_ELEVENTH_POST
    assert SARAFANOV_HOUSE_URL.replace("&", "&amp;") in formatted_text
    assert ">Кирова, 63</a>" in formatted_text


def test_viz_twelfth_post_is_available_and_formats_address_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_TWELFTH_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_TWELFTH_POST
    assert ASSUMPTION_CHURCH_URL.replace("&", "&amp;") in formatted_text
    assert ">Кирова, 65</a>" in formatted_text
