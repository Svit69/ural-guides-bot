from src.guides.viz_fifth_post import DEFAULT_VIZ_FIFTH_POST
from src.guides.viz_more_posts import DEFAULT_VIZ_FOURTH_POST, DEFAULT_VIZ_THIRD_POST
from src.guides.viz_posts import DEFAULT_VIZ_FIRST_POST, DEFAULT_VIZ_SECOND_POST
from src.guides.viz_posts import VIZ_FIFTH_POST_NUMBER, VIZ_FOURTH_POST_NUMBER
from src.guides.viz_posts import VIZ_FIRST_POST_NUMBER, VIZ_SECOND_POST_NUMBER
from src.guides.viz_posts import VIZ_SIXTH_POST_NUMBER, VIZ_THIRD_POST_NUMBER
from src.guides.viz_sixth_post import DEFAULT_VIZ_SIXTH_POST


class VizPostCatalog:
    def get_posts(self) -> dict[int, str]:
        return {
            VIZ_FIRST_POST_NUMBER: DEFAULT_VIZ_FIRST_POST,
            VIZ_SECOND_POST_NUMBER: DEFAULT_VIZ_SECOND_POST,
            VIZ_THIRD_POST_NUMBER: DEFAULT_VIZ_THIRD_POST,
            VIZ_FOURTH_POST_NUMBER: DEFAULT_VIZ_FOURTH_POST,
            VIZ_FIFTH_POST_NUMBER: DEFAULT_VIZ_FIFTH_POST,
            VIZ_SIXTH_POST_NUMBER: DEFAULT_VIZ_SIXTH_POST,
        }
