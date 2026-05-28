from src.messages.eighth_post import DEFAULT_EIGHTH_POST, HYDROELECTRIC_STATION_URL
from src.messages.seventh_post import DEFAULT_SEVENTH_POST, WOODEN_HOUSE_3_URL
from src.messages.seventh_post import WOODEN_HOUSE_4_URL
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_formats_seventh_post_address_links() -> None:
    assert_link(DEFAULT_SEVENTH_POST, WOODEN_HOUSE_3_URL, "Большеконный переулок, 3")
    assert_link(DEFAULT_SEVENTH_POST, WOODEN_HOUSE_4_URL, "Большеконный переулок, 4")


def test_formats_eighth_post_address_link() -> None:
    assert_link(DEFAULT_EIGHTH_POST, HYDROELECTRIC_STATION_URL, "Большой Конный полуостров, 5а")


def assert_link(source_text: str, url: str, text: str) -> None:
    result = TelegramTextFormatter().format_text(source_text)
    escaped_url = url.replace("&", "&amp;")

    assert f'<a href="{escaped_url}">{text}</a>' in result
