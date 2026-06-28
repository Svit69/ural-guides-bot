from src.guides.chekists_posts import CHEKISTS_FIFTH_POST_NUMBER, CHEKISTS_FIRST_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_EIGHTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_NINTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_SECOND_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_SEVENTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_SIXTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_TENTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_FOURTH_POST_NUMBER, CHEKISTS_THIRD_POST_NUMBER
from src.guides.chekists_art_posts import DEFAULT_CHEKISTS_TENTH_POST
from src.guides.chekists_building_posts import DEFAULT_CHEKISTS_EIGHTH_POST
from src.guides.chekists_building_posts import DEFAULT_CHEKISTS_NINTH_POST
from src.guides.chekists_posts import DEFAULT_CHEKISTS_FIRST_POST
from src.guides.chekists_posts import DEFAULT_CHEKISTS_SECOND_POST
from src.guides.chekists_food_posts import DEFAULT_CHEKISTS_SEVENTH_POST
from src.guides.chekists_food_posts import DEFAULT_CHEKISTS_SIXTH_POST
from src.guides.chekists_later_posts import DEFAULT_CHEKISTS_FIFTH_POST, DEFAULT_CHEKISTS_FOURTH_POST
from src.guides.chekists_later_posts import DEFAULT_CHEKISTS_THIRD_POST


class ChekistsPostCatalog:
    def get_posts(self) -> dict[int, str]:
        return {
            CHEKISTS_FIRST_POST_NUMBER: DEFAULT_CHEKISTS_FIRST_POST,
            CHEKISTS_SECOND_POST_NUMBER: DEFAULT_CHEKISTS_SECOND_POST,
            CHEKISTS_THIRD_POST_NUMBER: DEFAULT_CHEKISTS_THIRD_POST,
            CHEKISTS_FOURTH_POST_NUMBER: DEFAULT_CHEKISTS_FOURTH_POST,
            CHEKISTS_FIFTH_POST_NUMBER: DEFAULT_CHEKISTS_FIFTH_POST,
            CHEKISTS_SIXTH_POST_NUMBER: DEFAULT_CHEKISTS_SIXTH_POST,
            CHEKISTS_SEVENTH_POST_NUMBER: DEFAULT_CHEKISTS_SEVENTH_POST,
            CHEKISTS_EIGHTH_POST_NUMBER: DEFAULT_CHEKISTS_EIGHTH_POST,
            CHEKISTS_NINTH_POST_NUMBER: DEFAULT_CHEKISTS_NINTH_POST,
            CHEKISTS_TENTH_POST_NUMBER: DEFAULT_CHEKISTS_TENTH_POST,
        }
