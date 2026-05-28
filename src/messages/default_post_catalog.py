from src.messages.default_posts import DEFAULT_START_MESSAGE, SECOND_POST_NUMBER
from src.messages.default_posts import START_POST_NUMBER
from src.messages.second_post import DEFAULT_SECOND_POST


class DefaultPostCatalog:
    def get_default_text(self, post_number: int) -> str:
        defaults = {
            START_POST_NUMBER: DEFAULT_START_MESSAGE,
            SECOND_POST_NUMBER: DEFAULT_SECOND_POST,
        }
        return defaults.get(post_number, "")
