from src.messages.default_posts import DEFAULT_START_MESSAGE, SECOND_POST_NUMBER
from src.messages.default_posts import START_POST_NUMBER
from src.messages.default_posts import THIRD_POST_NUMBER
from src.messages.second_post import DEFAULT_SECOND_POST
from src.messages.third_post import DEFAULT_THIRD_POST


class DefaultPostCatalog:
    def get_default_text(self, post_number: int) -> str:
        defaults = {
            START_POST_NUMBER: DEFAULT_START_MESSAGE,
            SECOND_POST_NUMBER: DEFAULT_SECOND_POST,
            THIRD_POST_NUMBER: DEFAULT_THIRD_POST,
        }
        return defaults.get(post_number, "")
