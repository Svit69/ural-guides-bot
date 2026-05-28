from src.messages.default_posts import DEFAULT_START_MESSAGE
from src.messages.eleventh_post import DEFAULT_ELEVENTH_POST
from src.messages.eighth_post import DEFAULT_EIGHTH_POST
from src.messages.final_post import DEFAULT_FINAL_POST
from src.messages.fifth_post import DEFAULT_FIFTH_POST, HOUSE_COMMUNE_URL
from src.messages.fourth_post import ADDRESS_URL, DEFAULT_FOURTH_POST
from src.messages.ninth_post import DEFAULT_NINTH_POST
from src.messages.second_post import DEFAULT_SECOND_POST, YANDEX_ROUTE_URL
from src.messages.seventh_post import DEFAULT_SEVENTH_POST
from src.messages.sixth_post import DEFAULT_SIXTH_POST, FIRE_STATION_URL
from src.messages.tenth_post import DEFAULT_TENTH_POST
from src.messages.third_post import DEFAULT_THIRD_POST
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_default_posts_keep_readable_russian_text() -> None:
    all_posts = DEFAULT_START_MESSAGE + DEFAULT_SECOND_POST + DEFAULT_THIRD_POST
    all_posts += DEFAULT_FOURTH_POST + DEFAULT_FIFTH_POST + DEFAULT_SIXTH_POST
    all_posts += DEFAULT_SEVENTH_POST + DEFAULT_EIGHTH_POST + DEFAULT_NINTH_POST
    all_posts += DEFAULT_TENTH_POST + DEFAULT_ELEVENTH_POST + DEFAULT_FINAL_POST

    assert "Привет" in all_posts
    assert "На этом прогулка завершена" in all_posts
    assert "Рџ" not in all_posts


def test_formats_second_post_route_link() -> None:
    assert_link(DEFAULT_SECOND_POST, YANDEX_ROUTE_URL, "Тут ссылка.")


def test_formats_fourth_post_address_link() -> None:
    assert_link(DEFAULT_FOURTH_POST, ADDRESS_URL, "Большеконный переулок, 12")


def test_formats_fifth_post_address_link() -> None:
    assert_link(DEFAULT_FIFTH_POST, HOUSE_COMMUNE_URL, "Большеконный переулок, 10")


def test_formats_sixth_post_address_link() -> None:
    assert_link(DEFAULT_SIXTH_POST, FIRE_STATION_URL, " Большеконный переулок, 9")


def assert_link(source_text: str, url: str, text: str) -> None:
    result = TelegramTextFormatter().format_text(source_text)
    escaped_url = url.replace("&", "&amp;")

    assert f'<a href="{escaped_url}">{text}</a>' in result
