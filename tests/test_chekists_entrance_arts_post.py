from src.guides.chekists_library_posts import DEFAULT_CHEKISTS_THIRTY_FOURTH_POST
from src.guides.chekists_library_posts import ENTRANCE_ARTS_URL
from src.guides.chekists_posts import CHEKISTS_THIRTY_FOURTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_thirty_fourth_post_preserves_entrance_arts_link() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_THIRTY_FOURTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_THIRTY_FOURTH_POST
    assert f"*[Точка на карте({ENTRANCE_ARTS_URL})]*" in text
