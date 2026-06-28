from src.guides import chekists_posts as post


class ChekistsPostSelectionCatalog:
    def get_items(self) -> list[tuple[int, str]]:
        return [
            (post.CHEKISTS_FIRST_POST_NUMBER, "Старт"),
            (post.CHEKISTS_SECOND_POST_NUMBER, "Немного вводных"),
            (post.CHEKISTS_THIRD_POST_NUMBER, "Гостиница «Исеть»"),
            (post.CHEKISTS_FOURTH_POST_NUMBER, "Жилые корпуса"),
            (post.CHEKISTS_FIFTH_POST_NUMBER, "Граффити «Слово пацана»"),
            (post.CHEKISTS_SIXTH_POST_NUMBER, "Пончиковая №1"),
            (post.CHEKISTS_SEVENTH_POST_NUMBER, "Арт-объекты"),
            (post.CHEKISTS_EIGHTH_POST_NUMBER, "Хозкорпус"),
            (post.CHEKISTS_NINTH_POST_NUMBER, "Кофе с полынью"),
            (post.CHEKISTS_TENTH_POST_NUMBER, "5 арт-объектов"),
            (post.CHEKISTS_ELEVENTH_POST_NUMBER, "Шигирский идол"),
            (post.CHEKISTS_TWELFTH_POST_NUMBER, "Птицы на гараже"),
            (post.CHEKISTS_THIRTEENTH_POST_NUMBER, "Музей советского детства"),
            (post.CHEKISTS_FOURTEENTH_POST_NUMBER, "Птичка напела"),
            (post.CHEKISTS_FIFTEENTH_POST_NUMBER, "Второй идол"),
            (post.CHEKISTS_SIXTEENTH_POST_NUMBER, "Арт «Живи»"),
            (post.CHEKISTS_SEVENTEENTH_POST_NUMBER, "Третий идол"),
            (post.CHEKISTS_EIGHTEENTH_POST_NUMBER, "Четвертый идол"),
            (post.CHEKISTS_NINETEENTH_POST_NUMBER, "Пятый идол"),
            (post.CHEKISTS_TWENTIETH_POST_NUMBER, "Жилой дом"),
            (post.CHEKISTS_TWENTY_FIRST_POST_NUMBER, "Полянка"),
            (post.CHEKISTS_TWENTY_SECOND_POST_NUMBER, "Жилые дома"),
            (post.CHEKISTS_TWENTY_THIRD_POST_NUMBER, "Строчки из песни"),
            (post.CHEKISTS_TWENTY_FOURTH_POST_NUMBER, "Детский сад и ясли"),
        ]
