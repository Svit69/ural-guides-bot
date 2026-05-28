from src.text_formatting.formatter import TextFormatter
from src.text_formatting.html_helpers import wrap_blockquote
from src.text_formatting.inline_rules import HtmlTagRule, InlineFormattingRule
from src.text_formatting.link_parser import TelegramLinkParser


class TelegramTextFormatter(TextFormatter):
    def __init__(self) -> None:
        self.__link_parser = TelegramLinkParser()
        self.__inline_rules = self.__build_inline_rules()

    def format_text(self, source_text: str) -> str:
        paragraphs = source_text.split("\n\n")
        formatted_paragraphs = [self.__format_paragraph(item) for item in paragraphs]
        return "\n\n".join(formatted_paragraphs)

    def __format_paragraph(self, paragraph: str) -> str:
        if self.__is_quote(paragraph):
            quote_text = paragraph.strip()[1:-1]
            return wrap_blockquote(self.__format_inline_text(quote_text))
        return self.__format_inline_text(paragraph)

    def __format_inline_text(self, source_text: str) -> str:
        match_with_rule = self.__find_next_inline_match(source_text)
        if match_with_rule is None:
            return self.__link_parser.convert_links_to_html(source_text)
        match, rule = match_with_rule
        return "".join(
            [
                self.__format_inline_text(source_text[: match.start()]),
                rule.build_html(match.group(1), self.__format_inline_text),
                self.__format_inline_text(source_text[match.end() :]),
            ]
        )

    def __find_next_inline_match(self, source_text: str):
        matches = [
            (match, rule)
            for rule in self.__inline_rules
            if (match := rule.find_match(source_text)) is not None
        ]
        return min(matches, key=lambda item: item[0].start()) if matches else None

    def __build_inline_rules(self) -> list[InlineFormattingRule]:
        return [
            HtmlTagRule(r"```(.+?)```", "pre", False),
            HtmlTagRule(r"`([^`\n]+?)`", "code", False),
            HtmlTagRule(r"\|\|(.+?)\|\|", "tg-spoiler"),
            HtmlTagRule(r"__(.+?)__", "u"),
            HtmlTagRule(r"~(.+?)~", "s"),
            HtmlTagRule(r"\*(.+?)\*", "b"),
            HtmlTagRule(r"_(.+?)_", "i"),
        ]

    def __is_quote(self, paragraph: str) -> bool:
        stripped_paragraph = paragraph.strip()
        return stripped_paragraph.startswith("{") and stripped_paragraph.endswith("}")
