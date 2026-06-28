from src.guides.chekists_posts import CHEKISTS_FIFTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_EIGHTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_ELEVENTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_FIRST_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_FOURTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_NINTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_SECOND_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_SEVENTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_SIXTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_TENTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_THIRTEENTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_THIRD_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_TWELFTH_POST_NUMBER


class ChekistsPostSelectionCatalog:
    def get_items(self) -> list[tuple[int, str]]:
        return [
            (CHEKISTS_FIRST_POST_NUMBER, "Старт"),
            (CHEKISTS_SECOND_POST_NUMBER, "Немного вводных"),
            (CHEKISTS_THIRD_POST_NUMBER, "Гостиница «Исеть»"),
            (CHEKISTS_FOURTH_POST_NUMBER, "Жилые корпуса"),
            (CHEKISTS_FIFTH_POST_NUMBER, "Граффити «Слово пацана»"),
            (CHEKISTS_SIXTH_POST_NUMBER, "Пончиковая №1"),
            (CHEKISTS_SEVENTH_POST_NUMBER, "Арт-объекты"),
            (CHEKISTS_EIGHTH_POST_NUMBER, "Хозкорпус"),
            (CHEKISTS_NINTH_POST_NUMBER, "Кофе с полынью"),
            (CHEKISTS_TENTH_POST_NUMBER, "5 арт-объектов"),
            (CHEKISTS_ELEVENTH_POST_NUMBER, "Шигирский идол"),
            (CHEKISTS_TWELFTH_POST_NUMBER, "Птицы на гараже"),
            (CHEKISTS_THIRTEENTH_POST_NUMBER, "Музей советского детства"),
        ]
