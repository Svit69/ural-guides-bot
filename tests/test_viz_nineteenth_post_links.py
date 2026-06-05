from src.guides.viz_nineteenth_post import DEFAULT_VIZ_NINETEENTH_POST
from src.guides.viz_nineteenth_post import OLD_BELIEVERS_CHURCH_URL
from src.guides.viz_post_numbers import VIZ_NINETEENTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_viz_nineteenth_post_is_available_and_formats_address_link() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_NINETEENTH_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_NINETEENTH_POST
    assert OLD_BELIEVERS_CHURCH_URL.replace("&", "&amp;") in formatted_text
    assert ">Школьников, 1</a>" in formatted_text
