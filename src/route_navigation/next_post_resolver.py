from src.messages.default_posts import FIFTH_POST_NUMBER, FOURTH_POST_NUMBER
from src.messages.default_posts import SEVENTH_POST_NUMBER
from src.messages.default_posts import SIXTH_POST_NUMBER
from src.messages.default_posts import THIRD_POST_NUMBER


class NextPostResolver:
    def resolve_next_post(self, current_post_number: int) -> int | None:
        next_posts = {
            THIRD_POST_NUMBER: FOURTH_POST_NUMBER,
            FOURTH_POST_NUMBER: FIFTH_POST_NUMBER,
            FIFTH_POST_NUMBER: SIXTH_POST_NUMBER,
            SIXTH_POST_NUMBER: SEVENTH_POST_NUMBER,
        }
        return next_posts.get(current_post_number)
