from aiogram.types import Message, MessageEntity

from src.admin.message_text_extractor import AdminMessageTextExtractor


def test_extracts_telegram_text_link_as_editable_markup() -> None:
    message = Message(
        message_id=1,
        date=0,
        chat={"id": 1, "type": "private"},
        text="Тут ссылка",
        entities=[
            MessageEntity(
                type="text_link",
                offset=0,
                length=10,
                url="https://example.com",
            )
        ],
    )

    result = AdminMessageTextExtractor().extract_editable_text(message)

    assert result == "[Тут ссылка (https://example.com)]"


def test_preserves_bold_text_link_as_nested_markup() -> None:
    message = Message(
        message_id=1,
        date=0,
        chat={"id": 1, "type": "private"},
        text="Тут",
        entities=[
            MessageEntity(type="bold", offset=0, length=3),
            MessageEntity(type="text_link", offset=0, length=3, url="https://t.me/nast_bar"),
        ],
    )

    result = AdminMessageTextExtractor().extract_editable_text(message)

    assert result == "*[Тут (https://t.me/nast_bar)]*"
