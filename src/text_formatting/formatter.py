from abc import ABC, abstractmethod


class TextFormatter(ABC):
    @abstractmethod
    def format_text(self, source_text: str) -> str:
        """Convert source markup into target message markup."""
