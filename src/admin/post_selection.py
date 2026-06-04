from src.admin.callbacks import AdminCallbackData
from src.guides.viz_posts import VIZ_FIFTH_POST_NUMBER
from src.guides.viz_posts import VIZ_SIXTH_POST_NUMBER
from src.guides.viz_posts import VIZ_FOURTH_POST_NUMBER
from src.guides.viz_posts import VIZ_FIRST_POST_NUMBER, VIZ_SECOND_POST_NUMBER
from src.guides.viz_posts import VIZ_THIRD_POST_NUMBER
from src.messages.default_posts import ELEVENTH_POST_NUMBER, EIGHTH_POST_NUMBER
from src.messages.default_posts import FIFTH_POST_NUMBER, FINAL_POST_NUMBER
from src.messages.default_posts import FOURTH_POST_NUMBER, NINTH_POST_NUMBER
from src.messages.default_posts import SECOND_POST_NUMBER, SEVENTH_POST_NUMBER
from src.messages.default_posts import SIXTH_POST_NUMBER, START_POST_NUMBER
from src.messages.default_posts import TENTH_POST_NUMBER, THIRD_POST_NUMBER


class PostSelectionCatalog:
    def get_items_for_guide(self, guide_id: str) -> list[tuple[int, str]]:
        if guide_id == AdminCallbackData.GUIDE_VIZ:
            return self.__get_viz_items()
        return self.__get_big_konny_items()

    def contains_post(self, guide_id: str, post_number: int) -> bool:
        return any(number == post_number for number, _ in self.get_items_for_guide(guide_id))

    def __get_viz_items(self) -> list[tuple[int, str]]:
        return [
            (VIZ_FIRST_POST_NUMBER, "Первый пост"),
            (VIZ_SECOND_POST_NUMBER, "Дворец молодёжи"),
            (VIZ_THIRD_POST_NUMBER, "Парк 22 Партсъезда"),
            (VIZ_FOURTH_POST_NUMBER, "Синара-Центр"),
            (VIZ_FIFTH_POST_NUMBER, "Верх-Исетский бульвар"),
            (VIZ_SIXTH_POST_NUMBER, "Дом для заводчан"),
        ]

    def __get_big_konny_items(self) -> list[tuple[int, str]]:
        return [
            (START_POST_NUMBER, "Приветствие"),
            (SECOND_POST_NUMBER, "Площадь Субботников"),
            (THIRD_POST_NUMBER, "Зеленый остров"),
            (FOURTH_POST_NUMBER, "Большеконный, 12"),
            (FIFTH_POST_NUMBER, "Дом-коммуна"),
            (SIXTH_POST_NUMBER, "Бывшая пожарная часть"),
            (SEVENTH_POST_NUMBER, "Деревянные домики"),
            (EIGHTH_POST_NUMBER, "Свердловская ГЭС"),
            (NINTH_POST_NUMBER, "Памятник Куйбышеву"),
            (TENTH_POST_NUMBER, "Здание у пляжа"),
            (ELEVENTH_POST_NUMBER, "Арт-объекты"),
            (FINAL_POST_NUMBER, "Финальный пост"),
        ]
