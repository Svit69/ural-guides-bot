from src.text_formatting.inline_rules import HtmlTagRule, InlineFormattingRule


class InlineRuleCatalog:
    def build_inline_rules(self) -> list[InlineFormattingRule]:
        return [
            HtmlTagRule(r"```(.+?)```", "pre", False),
            HtmlTagRule(r"`([^`\n]+?)`", "code", False),
            HtmlTagRule(r"\|\|(.+?)\|\|", "tg-spoiler"),
            HtmlTagRule(r"__(.+?)__", "u"),
            HtmlTagRule(r"~(.+?)~", "s"),
            HtmlTagRule(r"\*(.+?)\*", "b"),
            HtmlTagRule(r"_(.+?)_", "i"),
        ]
