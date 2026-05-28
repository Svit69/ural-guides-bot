import re
from abc import ABC, abstractmethod
from collections.abc import Callable

from src.text_formatting.html_helpers import escape_telegram_html


class InlineFormattingRule(ABC):
    def __init__(self, pattern: str, supports_nested_markup: bool = True) -> None:
        self.__pattern = re.compile(pattern, re.DOTALL)
        self.__supports_nested_markup = supports_nested_markup

    def find_match(self, source_text: str) -> re.Match[str] | None:
        return self.__pattern.search(source_text)

    def build_html(self, content: str, formatter: Callable[[str], str]) -> str:
        value = (
            formatter(content)
            if self.__supports_nested_markup
            else escape_telegram_html(content)
        )
        return self.wrap_formatted_content(value)

    @abstractmethod
    def wrap_formatted_content(self, content: str) -> str:
        """Wrap already formatted content with a Telegram HTML tag."""


class HtmlTagRule(InlineFormattingRule):
    def __init__(
        self, pattern: str, tag_name: str, supports_nested_markup: bool = True
    ) -> None:
        super().__init__(pattern, supports_nested_markup)
        self.__tag_name = tag_name

    def wrap_formatted_content(self, content: str) -> str:
        return f"<{self.__tag_name}>{content}</{self.__tag_name}>"
