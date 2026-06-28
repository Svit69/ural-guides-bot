from src.guides.chekists_extra_art_posts import DEFAULT_CHEKISTS_EIGHTEENTH_POST
from src.guides.chekists_extra_art_posts import FOURTH_IDOL_URL
from src.guides.chekists_posts import CHEKISTS_EIGHTEENTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_eighteenth_post_preserves_map_link() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_EIGHTEENTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_EIGHTEENTH_POST
    assert f"*[Точка на карте({FOURTH_IDOL_URL})]*" in text
