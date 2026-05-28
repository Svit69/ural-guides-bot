class InlineMatchFinder:
    def __init__(self, inline_rules) -> None:
        self.__inline_rules = inline_rules

    def find_next_inline_match(self, source_text: str):
        matches = [
            (match, rule)
            for rule in self.__inline_rules
            if (match := rule.find_match(source_text)) is not None
        ]
        return min(matches, key=lambda item: item[0].start()) if matches else None

    def is_link_before_rule(self, link_match, match_with_rule) -> bool:
        if match_with_rule is None:
            return True
        return link_match.start() < match_with_rule[0].start()
