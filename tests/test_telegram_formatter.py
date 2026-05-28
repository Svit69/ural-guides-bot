from src.text_formatting.telegram_formatter import TelegramTextFormatter
from src.messages.default_posts import DEFAULT_START_MESSAGE


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

    result = formatter.format_text(
        "_курсив_ __низ__ ~нет~ ||тайна|| `x < y` ```print('ok')```"
    )

    assert result == (
        "<i>курсив</i> <u>низ</u> <s>нет</s> "
        "<tg-spoiler>тайна</tg-spoiler> <code>x &lt; y</code> "
        "<pre>print('ok')</pre>"
    )


def test_default_start_message_keeps_readable_russian_text() -> None:
    assert "Привет" in DEFAULT_START_MESSAGE
    assert "Рџ" not in DEFAULT_START_MESSAGE
