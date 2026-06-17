from src.admin.callbacks import AdminCallbackData
from src.guides.city_walk_post import CITY_WALK_POST_NUMBER
from src.admin.viz_post_selection import VizPostSelectionCatalog
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
        if guide_id == AdminCallbackData.GUIDE_CITY_WALK:
            return [(CITY_WALK_POST_NUMBER, "Прогулка по Екатеринбургу")]
        return self.__get_big_konny_items()

    def contains_post(self, guide_id: str, post_number: int) -> bool:
        return any(number == post_number for number, _ in self.get_items_for_guide(guide_id))

    def __get_viz_items(self) -> list[tuple[int, str]]:
        return VizPostSelectionCatalog().get_items()

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
