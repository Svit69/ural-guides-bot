from src.guides.viz_eighteenth_post import DEFAULT_VIZ_EIGHTEENTH_POST
from src.guides.viz_fifteenth_post import DEFAULT_VIZ_FIFTEENTH_POST
from src.guides.viz_fourteenth_post import DEFAULT_VIZ_FOURTEENTH_POST
from src.guides.viz_nineteenth_post import DEFAULT_VIZ_NINETEENTH_POST
from src.guides.viz_post_numbers import VIZ_EIGHTEENTH_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_FIFTEENTH_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_FOURTEENTH_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_NINETEENTH_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_SEVENTEENTH_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_SIXTEENTH_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_THIRTEENTH_POST_NUMBER
from src.guides.viz_seventeenth_post import DEFAULT_VIZ_SEVENTEENTH_POST
from src.guides.viz_sixteenth_post import DEFAULT_VIZ_SIXTEENTH_POST
from src.guides.viz_thirteenth_post import DEFAULT_VIZ_THIRTEENTH_POST
from src.guides.viz_twentieth_post import DEFAULT_VIZ_TWENTIETH_POST
from src.guides.viz_post_numbers import VIZ_TWENTIETH_POST_NUMBER


class VizLatePostCatalog:
    def get_posts(self) -> dict[int, str]:
        return {
            VIZ_THIRTEENTH_POST_NUMBER: DEFAULT_VIZ_THIRTEENTH_POST,
            VIZ_FOURTEENTH_POST_NUMBER: DEFAULT_VIZ_FOURTEENTH_POST,
            VIZ_FIFTEENTH_POST_NUMBER: DEFAULT_VIZ_FIFTEENTH_POST,
            VIZ_SIXTEENTH_POST_NUMBER: DEFAULT_VIZ_SIXTEENTH_POST,
            VIZ_SEVENTEENTH_POST_NUMBER: DEFAULT_VIZ_SEVENTEENTH_POST,
            VIZ_EIGHTEENTH_POST_NUMBER: DEFAULT_VIZ_EIGHTEENTH_POST,
            VIZ_NINETEENTH_POST_NUMBER: DEFAULT_VIZ_NINETEENTH_POST,
            VIZ_TWENTIETH_POST_NUMBER: DEFAULT_VIZ_TWENTIETH_POST,
        }
