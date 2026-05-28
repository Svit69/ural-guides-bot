class MessageChunks:
    __telegram_text_limit = 4096

    def split_text(self, text: str) -> list[str]:
        if len(text) <= self.__telegram_text_limit:
            return [text]
        chunks: list[str] = []
        current_chunk = ""
        for line in text.splitlines():
            if len(current_chunk) + len(line) + 1 > self.__telegram_text_limit:
                chunks.append(current_chunk)
                current_chunk = line
                continue
            current_chunk = f"{current_chunk}\n{line}" if current_chunk else line
        if current_chunk:
            chunks.append(current_chunk)
        return chunks
