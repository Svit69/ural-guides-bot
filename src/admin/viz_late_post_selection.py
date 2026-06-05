from src.guides.viz_post_numbers import VIZ_EIGHTEENTH_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_NINETEENTH_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_TWENTIETH_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_TWENTY_FIFTH_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_TWENTY_FIRST_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_TWENTY_FOURTH_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_TWENTY_SECOND_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_TWENTY_THIRD_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_TWENTY_SIXTH_POST_NUMBER
from src.guides.viz_posts import VIZ_FIFTEENTH_POST_NUMBER
from src.guides.viz_posts import VIZ_SEVENTEENTH_POST_NUMBER
from src.guides.viz_posts import VIZ_SIXTEENTH_POST_NUMBER


class VizLatePostSelectionCatalog:
    def get_items(self) -> list[tuple[int, str]]:
        return [
            (VIZ_FIFTEENTH_POST_NUMBER, "ДК «Верх-Исетский»"),
            (VIZ_SIXTEENTH_POST_NUMBER, "Площадь Субботников"),
            (VIZ_SEVENTEENTH_POST_NUMBER, "Столовая"),
            (VIZ_EIGHTEENTH_POST_NUMBER, "Следующая карта"),
            (VIZ_NINETEENTH_POST_NUMBER, "Старообрядческая церковь"),
            (VIZ_TWENTIETH_POST_NUMBER, "Пруд на ВИЗе"),
            (VIZ_TWENTY_FIRST_POST_NUMBER, "Индустриальный младенец"),
            (VIZ_TWENTY_SECOND_POST_NUMBER, "Рынок на Заводской"),
            (VIZ_TWENTY_THIRD_POST_NUMBER, "Китайская стена"),
            (VIZ_TWENTY_FOURTH_POST_NUMBER, "Дом за 58 часов"),
            (VIZ_TWENTY_FIFTH_POST_NUMBER, "Старая лиственница"),
            (VIZ_TWENTY_SIXTH_POST_NUMBER, "Гастроном 2"),
        ]
