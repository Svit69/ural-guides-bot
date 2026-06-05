from src.guides.viz_posts import VIZ_EIGHTH_POST_NUMBER, VIZ_FIFTH_POST_NUMBER
from src.guides.viz_posts import VIZ_ELEVENTH_POST_NUMBER
from src.guides.viz_posts import VIZ_FIFTEENTH_POST_NUMBER
from src.guides.viz_posts import VIZ_FOURTEENTH_POST_NUMBER
from src.guides.viz_posts import VIZ_FIRST_POST_NUMBER, VIZ_FOURTH_POST_NUMBER
from src.guides.viz_posts import VIZ_NINTH_POST_NUMBER, VIZ_SECOND_POST_NUMBER
from src.guides.viz_posts import VIZ_SEVENTH_POST_NUMBER, VIZ_SIXTH_POST_NUMBER
from src.guides.viz_posts import VIZ_SIXTEENTH_POST_NUMBER
from src.guides.viz_posts import VIZ_TENTH_POST_NUMBER, VIZ_THIRD_POST_NUMBER
from src.guides.viz_posts import VIZ_THIRTEENTH_POST_NUMBER
from src.guides.viz_posts import VIZ_TWELFTH_POST_NUMBER


class VizPostSelectionCatalog:
    def get_items(self) -> list[tuple[int, str]]:
        return [
            (VIZ_FIRST_POST_NUMBER, "Первый пост"),
            (VIZ_SECOND_POST_NUMBER, "Дворец молодёжи"),
            (VIZ_THIRD_POST_NUMBER, "Парк 22 Партсъезда"),
            (VIZ_FOURTH_POST_NUMBER, "Синара-Центр"),
            (VIZ_FIFTH_POST_NUMBER, "Верх-Исетский бульвар"),
            (VIZ_SIXTH_POST_NUMBER, "Дом для заводчан"),
            (VIZ_SEVENTH_POST_NUMBER, "Булочная"),
            (VIZ_EIGHTH_POST_NUMBER, "Каменный дом"),
            (VIZ_NINTH_POST_NUMBER, "Деревянный дом"),
            (VIZ_TENTH_POST_NUMBER, "Арт-объект «Визмут»"),
            (VIZ_ELEVENTH_POST_NUMBER, "Дом М. М. Сарафанова"),
            (VIZ_TWELFTH_POST_NUMBER, "Храм Успения"),
            (VIZ_THIRTEENTH_POST_NUMBER, "Трапезная при храме"),
            (VIZ_FOURTEENTH_POST_NUMBER, "Дом-музей «Успенский»"),
            (VIZ_FIFTEENTH_POST_NUMBER, "ДК «Верх-Исетский»"),
            (VIZ_SIXTEENTH_POST_NUMBER, "Площадь Субботников"),
        ]
