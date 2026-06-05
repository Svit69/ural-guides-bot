from src.guides.viz_post_numbers import VIZ_TWENTY_FOURTH_POST_NUMBER
from src.guides.viz_twenty_fourth_post import DEFAULT_VIZ_TWENTY_FOURTH_POST
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_viz_twenty_fourth_post_is_available_and_formats_title() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_TWENTY_FOURTH_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_TWENTY_FOURTH_POST
    assert "<b>Дом, который построили за 58 часов | Крауля, 72</b>" in formatted_text
