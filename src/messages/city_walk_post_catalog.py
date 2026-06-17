from src.guides.city_walk_post import CITY_WALK_POST_NUMBER
from src.guides.city_walk_post import DEFAULT_CITY_WALK_POST


class CityWalkPostCatalog:
    def get_posts(self) -> dict[int, str]:
        return {CITY_WALK_POST_NUMBER: DEFAULT_CITY_WALK_POST}
