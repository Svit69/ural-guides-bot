from src.guides.chekists_posts import CHEKISTS_FIRST_POST_NUMBER
from src.guides.chekists_posts import DEFAULT_CHEKISTS_FIRST_POST


class ChekistsPostCatalog:
    def get_posts(self) -> dict[int, str]:
        return {CHEKISTS_FIRST_POST_NUMBER: DEFAULT_CHEKISTS_FIRST_POST}
