class TelegramEntityOffsetMapper:
    def build_python_index_map(self, text: str) -> dict[int, int]:
        result: dict[int, int] = {}
        offset = 0
        for index, char in enumerate(text):
            result[offset] = index
            offset += len(char.encode("utf-16-le")) // 2
        result[offset] = len(text)
        return result
