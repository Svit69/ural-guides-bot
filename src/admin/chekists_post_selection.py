from src.guides.chekists_posts import CHEKISTS_FIFTH_POST_NUMBER, CHEKISTS_FIRST_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_FOURTH_POST_NUMBER, CHEKISTS_SECOND_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_THIRD_POST_NUMBER


class ChekistsPostSelectionCatalog:
    def get_items(self) -> list[tuple[int, str]]:
        return [
            (CHEKISTS_FIRST_POST_NUMBER, "Старт"),
            (CHEKISTS_SECOND_POST_NUMBER, "Немного вводных"),
            (CHEKISTS_THIRD_POST_NUMBER, "Гостиница «Исеть»"),
            (CHEKISTS_FOURTH_POST_NUMBER, "Жилые корпуса"),
            (CHEKISTS_FIFTH_POST_NUMBER, "Граффити «Слово пацана»"),
        ]
