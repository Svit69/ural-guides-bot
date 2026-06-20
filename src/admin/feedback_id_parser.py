class FeedbackIdParser:
    def parse_ids(self, raw_value: str | None) -> list[int]:
        if raw_value is None:
            return []
        values: list[int] = []
        for part in raw_value.split(","):
            value = part.strip()
            if not value.isdigit():
                return []
            values.append(int(value))
        return list(dict.fromkeys(values))
