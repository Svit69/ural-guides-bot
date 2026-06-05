from src.guides.viz_fifth_post import DEFAULT_VIZ_FIFTH_POST
from src.guides.viz_eighth_post import DEFAULT_VIZ_EIGHTH_POST
from src.guides.viz_eleventh_post import DEFAULT_VIZ_ELEVENTH_POST
from src.guides.viz_ninth_post import DEFAULT_VIZ_NINTH_POST
from src.guides.viz_tenth_post import DEFAULT_VIZ_TENTH_POST
from src.guides.viz_twelfth_post import DEFAULT_VIZ_TWELFTH_POST
from src.guides.viz_more_posts import DEFAULT_VIZ_FOURTH_POST, DEFAULT_VIZ_THIRD_POST
from src.guides.viz_posts import DEFAULT_VIZ_FIRST_POST, DEFAULT_VIZ_SECOND_POST
from src.guides.viz_posts import VIZ_FIFTH_POST_NUMBER, VIZ_FOURTH_POST_NUMBER
from src.guides.viz_posts import VIZ_EIGHTH_POST_NUMBER
from src.guides.viz_posts import VIZ_ELEVENTH_POST_NUMBER
from src.guides.viz_posts import VIZ_NINTH_POST_NUMBER
from src.guides.viz_posts import VIZ_TENTH_POST_NUMBER
from src.guides.viz_posts import VIZ_TWELFTH_POST_NUMBER
from src.guides.viz_posts import VIZ_FIRST_POST_NUMBER, VIZ_SECOND_POST_NUMBER
from src.guides.viz_posts import VIZ_SIXTH_POST_NUMBER, VIZ_THIRD_POST_NUMBER
from src.guides.viz_sixth_post import DEFAULT_VIZ_SIXTH_POST
from src.guides.viz_seventh_post import DEFAULT_VIZ_SEVENTH_POST
from src.guides.viz_posts import VIZ_SEVENTH_POST_NUMBER


class VizPostCatalog:
    def get_posts(self) -> dict[int, str]:
        return {
            VIZ_FIRST_POST_NUMBER: DEFAULT_VIZ_FIRST_POST,
            VIZ_SECOND_POST_NUMBER: DEFAULT_VIZ_SECOND_POST,
            VIZ_THIRD_POST_NUMBER: DEFAULT_VIZ_THIRD_POST,
            VIZ_FOURTH_POST_NUMBER: DEFAULT_VIZ_FOURTH_POST,
            VIZ_FIFTH_POST_NUMBER: DEFAULT_VIZ_FIFTH_POST,
            VIZ_SIXTH_POST_NUMBER: DEFAULT_VIZ_SIXTH_POST,
            VIZ_SEVENTH_POST_NUMBER: DEFAULT_VIZ_SEVENTH_POST,
            VIZ_EIGHTH_POST_NUMBER: DEFAULT_VIZ_EIGHTH_POST,
            VIZ_NINTH_POST_NUMBER: DEFAULT_VIZ_NINTH_POST,
            VIZ_TENTH_POST_NUMBER: DEFAULT_VIZ_TENTH_POST,
            VIZ_ELEVENTH_POST_NUMBER: DEFAULT_VIZ_ELEVENTH_POST,
            VIZ_TWELFTH_POST_NUMBER: DEFAULT_VIZ_TWELFTH_POST,
        }
