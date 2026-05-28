from src.messages.default_posts import DEFAULT_START_MESSAGE
from src.messages.fifth_post import DEFAULT_FIFTH_POST, HOUSE_COMMUNE_URL
from src.messages.fourth_post import ADDRESS_URL, DEFAULT_FOURTH_POST
from src.messages.second_post import DEFAULT_SECOND_POST, YANDEX_ROUTE_URL
from src.messages.sixth_post import DEFAULT_SIXTH_POST, FIRE_STATION_URL
from src.messages.third_post import DEFAULT_THIRD_POST
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_default_posts_keep_readable_russian_text() -> None:
    assert "Привет" in DEFAULT_START_MESSAGE
    assert "Cтарт на Площади Субботников" in DEFAULT_SECOND_POST
    assert "Выходим на конечной" in DEFAULT_THIRD_POST
    assert "Один из первых домов" in DEFAULT_FOURTH_POST
    assert "Дом-коммуна" in DEFAULT_FIFTH_POST
    assert "Бывшая пожарная часть" in DEFAULT_SIXTH_POST
    all_posts = DEFAULT_START_MESSAGE + DEFAULT_SECOND_POST + DEFAULT_THIRD_POST
    all_posts += DEFAULT_FOURTH_POST + DEFAULT_FIFTH_POST + DEFAULT_SIXTH_POST
    assert "Рџ" not in all_posts


def test_formats_second_post_route_link() -> None:
    result = TelegramTextFormatter().format_text(DEFAULT_SECOND_POST)
    escaped_url = YANDEX_ROUTE_URL.replace("&", "&amp;")

    assert YANDEX_ROUTE_URL.endswith("rtt=pd")
    assert f'<a href="{escaped_url}">Тут ссылка.</a>' in result


def test_formats_fourth_post_address_link() -> None:
    result = TelegramTextFormatter().format_text(DEFAULT_FOURTH_POST)
    escaped_url = ADDRESS_URL.replace("&", "&amp;")

    assert f'<a href="{escaped_url}">Большеконный переулок, 12</a>' in result


def test_formats_fifth_post_address_link() -> None:
    result = TelegramTextFormatter().format_text(DEFAULT_FIFTH_POST)
    escaped_url = HOUSE_COMMUNE_URL.replace("&", "&amp;")

    assert f'<a href="{escaped_url}">Большеконный переулок, 10</a>' in result


def test_formats_sixth_post_address_link() -> None:
    result = TelegramTextFormatter().format_text(DEFAULT_SIXTH_POST)
    escaped_url = FIRE_STATION_URL.replace("&", "&amp;")

    assert f'<a href="{escaped_url}"> Большеконный переулок, 9</a>' in result
