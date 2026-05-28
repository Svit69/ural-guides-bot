from src.messages.default_posts import DEFAULT_START_MESSAGE
from src.messages.fourth_post import ADDRESS_URL, DEFAULT_FOURTH_POST
from src.messages.second_post import DEFAULT_SECOND_POST, YANDEX_ROUTE_URL
from src.messages.third_post import DEFAULT_THIRD_POST
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_formats_bold_link_and_quote() -> None:
    formatter = TelegramTextFormatter()

    result = formatter.format_text("*[пример (https://example.com)]*\n\n{цитата}")

    assert result == (
        '<b><a href="https://example.com">пример</a></b>'
        "\n\n<blockquote>цитата</blockquote>"
    )


def test_preserves_emoji_and_paragraph_spacing() -> None:
    formatter = TelegramTextFormatter()

    result = formatter.format_text("Привет 👋🏻\n\n\nПогнали!")

    assert result == "Привет 👋🏻\n\n\nПогнали!"


def test_formats_telegram_inline_styles() -> None:
    formatter = TelegramTextFormatter()
    result = formatter.format_text("_курсив_ __низ__ ~нет~ ||тайна|| `x < y`")

    assert result == (
        "<i>курсив</i> <u>низ</u> <s>нет</s> "
        "<tg-spoiler>тайна</tg-spoiler> <code>x &lt; y</code>"
    )


def test_default_posts_keep_readable_russian_text() -> None:
    assert "Привет" in DEFAULT_START_MESSAGE
    assert "Cтарт на Площади Субботников" in DEFAULT_SECOND_POST
    assert "Выходим на конечной" in DEFAULT_THIRD_POST
    assert "Один из первых домов" in DEFAULT_FOURTH_POST
    all_default_posts = DEFAULT_START_MESSAGE + DEFAULT_SECOND_POST
    all_default_posts += DEFAULT_THIRD_POST + DEFAULT_FOURTH_POST
    assert "Рџ" not in all_default_posts


def test_formats_second_post_route_link() -> None:
    formatter = TelegramTextFormatter()
    result = formatter.format_text(DEFAULT_SECOND_POST)
    escaped_url = YANDEX_ROUTE_URL.replace("&", "&amp;")

    assert YANDEX_ROUTE_URL.endswith("rtt=pd")
    assert f'<a href="{escaped_url}">Тут ссылка.</a>' in result


def test_formats_fourth_post_address_link() -> None:
    formatter = TelegramTextFormatter()
    result = formatter.format_text(DEFAULT_FOURTH_POST)
    escaped_url = ADDRESS_URL.replace("&", "&amp;")

    assert f'<a href="{escaped_url}">Большеконный переулок, 12</a>' in result
