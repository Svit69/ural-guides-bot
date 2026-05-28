from src.messages.default_posts import DEFAULT_START_MESSAGE, SECOND_POST_NUMBER
from src.messages.default_posts import ELEVENTH_POST_NUMBER
from src.messages.default_posts import EIGHTH_POST_NUMBER
from src.messages.default_posts import FINAL_POST_NUMBER
from src.messages.default_posts import FIFTH_POST_NUMBER
from src.messages.default_posts import FOURTH_POST_NUMBER
from src.messages.default_posts import NINTH_POST_NUMBER
from src.messages.default_posts import SEVENTH_POST_NUMBER
from src.messages.default_posts import SIXTH_POST_NUMBER
from src.messages.default_posts import START_POST_NUMBER
from src.messages.default_posts import TENTH_POST_NUMBER
from src.messages.default_posts import THIRD_POST_NUMBER
from src.messages.eleventh_post import DEFAULT_ELEVENTH_POST
from src.messages.eighth_post import DEFAULT_EIGHTH_POST
from src.messages.final_post import DEFAULT_FINAL_POST
from src.messages.fifth_post import DEFAULT_FIFTH_POST
from src.messages.fourth_post import DEFAULT_FOURTH_POST
from src.messages.ninth_post import DEFAULT_NINTH_POST
from src.messages.second_post import DEFAULT_SECOND_POST
from src.messages.seventh_post import DEFAULT_SEVENTH_POST
from src.messages.sixth_post import DEFAULT_SIXTH_POST
from src.messages.tenth_post import DEFAULT_TENTH_POST
from src.messages.third_post import DEFAULT_THIRD_POST


class DefaultPostCatalog:
    def get_default_text(self, post_number: int) -> str:
        defaults = {
            START_POST_NUMBER: DEFAULT_START_MESSAGE,
            SECOND_POST_NUMBER: DEFAULT_SECOND_POST,
            THIRD_POST_NUMBER: DEFAULT_THIRD_POST,
            FOURTH_POST_NUMBER: DEFAULT_FOURTH_POST,
            FIFTH_POST_NUMBER: DEFAULT_FIFTH_POST,
            SIXTH_POST_NUMBER: DEFAULT_SIXTH_POST,
            SEVENTH_POST_NUMBER: DEFAULT_SEVENTH_POST,
            EIGHTH_POST_NUMBER: DEFAULT_EIGHTH_POST,
            NINTH_POST_NUMBER: DEFAULT_NINTH_POST,
            TENTH_POST_NUMBER: DEFAULT_TENTH_POST,
            ELEVENTH_POST_NUMBER: DEFAULT_ELEVENTH_POST,
            FINAL_POST_NUMBER: DEFAULT_FINAL_POST,
        }
        return defaults.get(post_number, "")
