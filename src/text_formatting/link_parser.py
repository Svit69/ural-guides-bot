import re

from src.text_formatting.html_helpers import escape_telegram_html, wrap_link


class TelegramLinkParser:
    __link_pattern = re.compile(r"\[([^\[\]\n]+?)\s+\((https?://[^)\s]+)\)\]")

    def convert_links_to_html(self, source_text: str) -> str:
        result_parts: list[str] = []
        cursor_position = 0
        for match in self.__link_pattern.finditer(source_text):
            result_parts.append(
                escape_telegram_html(source_text[cursor_position : match.start()])
            )
            result_parts.append(self.__build_link_html(match))
            cursor_position = match.end()
        result_parts.append(escape_telegram_html(source_text[cursor_position:]))
        return "".join(result_parts)

    def __build_link_html(self, match: re.Match[str]) -> str:
        text = escape_telegram_html(match.group(1))
        return wrap_link(text, match.group(2))
