from src.guides.chekists_extra_art_posts import BIRD_SANG_HOUSE_URL
from src.guides.chekists_extra_art_posts import DEFAULT_CHEKISTS_FOURTEENTH_POST
from src.guides.chekists_posts import CHEKISTS_FOURTEENTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_fourteenth_post_preserves_neighbor_house_link() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_FOURTEENTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_FOURTEENTH_POST
    assert f"[соседнего дома]({BIRD_SANG_HOUSE_URL})" in text
