from aiogram.types import Message, MessageEntity

from src.admin.entity_offsets import TelegramEntityOffsetMapper


class AdminMessageTextExtractor:
    def __init__(self) -> None:
        self.__offset_mapper = TelegramEntityOffsetMapper()

    def extract_editable_text(self, message: Message) -> str:
        text = message.text or ""
        entities = list(message.entities or [])
        if not text or not entities:
            return text
        return self.__apply_entities(text, entities)

    def __apply_entities(self, text: str, entities: list[MessageEntity]) -> str:
        index_map = self.__offset_mapper.build_python_index_map(text)
        grouped = self.__group_entities(entities)
        for offset, length in sorted(grouped.keys(), reverse=True):
            start = index_map[offset]
            end = index_map[offset + length]
            replacement = self.__format_value(text[start:end], grouped[(offset, length)])
            text = f"{text[:start]}{replacement}{text[end:]}"
        return text

    def __group_entities(self, entities: list[MessageEntity]) -> dict[tuple[int, int], list[MessageEntity]]:
        result: dict[tuple[int, int], list[MessageEntity]] = {}
        for entity in entities:
            result.setdefault((entity.offset, entity.length), []).append(entity)
        return result

    def __format_value(self, value: str, entities: list[MessageEntity]) -> str:
        for entity in sorted(entities, key=lambda item: self.__priority(item.type)):
            value = self.__wrap_value(value, entity)
        return value

    def __wrap_value(self, value: str, entity: MessageEntity) -> str:
        markers = {"bold": "*", "italic": "_", "underline": "__", "strikethrough": "~", "spoiler": "||", "code": "`", "pre": "```"}
        if entity.type == "text_link" and entity.url:
            return f"[{value} ({entity.url})]"
        if entity.type == "url":
            return f"[{value} ({value})]"
        if entity.type == "blockquote":
            return f"{{{value}}}"
        marker = markers.get(entity.type)
        return f"{marker}{value}{marker}" if marker else value

    def __priority(self, entity_type: str) -> int:
        return 0 if entity_type in {"text_link", "url"} else 1
