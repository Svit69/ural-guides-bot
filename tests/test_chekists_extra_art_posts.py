from src.guides.chekists_extra_art_posts import BIRD_SANG_HOUSE_URL
from src.guides.chekists_extra_art_posts import DEFAULT_CHEKISTS_FIFTEENTH_POST
from src.guides.chekists_extra_art_posts import DEFAULT_CHEKISTS_FOURTEENTH_POST
from src.guides.chekists_extra_art_posts import DEFAULT_CHEKISTS_SEVENTEENTH_POST
from src.guides.chekists_extra_art_posts import DEFAULT_CHEKISTS_SIXTEENTH_POST
from src.guides.chekists_extra_art_posts import HOUSE_14_ENTRANCE_URL
from src.guides.chekists_extra_art_posts import SECOND_IDOL_URL, THIRD_IDOL_URL
from src.guides.chekists_posts import CHEKISTS_FIFTEENTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_FOURTEENTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_SEVENTEENTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_SIXTEENTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_fourteenth_post_preserves_neighbor_house_link() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_FOURTEENTH_POST_NUMBER)
    assert text == DEFAULT_CHEKISTS_FOURTEENTH_POST
    assert f"[соседнего дома]({BIRD_SANG_HOUSE_URL})" in text


def test_chekists_fifteenth_post_preserves_map_link() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_FIFTEENTH_POST_NUMBER)
    assert text == DEFAULT_CHEKISTS_FIFTEENTH_POST
    assert f"[Точка на карте]({SECOND_IDOL_URL})" in text


def test_chekists_sixteenth_post_preserves_link_and_emoji() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_SIXTEENTH_POST_NUMBER)
    assert text == DEFAULT_CHEKISTS_SIXTEENTH_POST
    assert f"[попасть в подъезд]({HOUSE_14_ENTRANCE_URL})" in text
    assert "💔" in text


def test_chekists_seventeenth_post_preserves_link_and_emoji() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_SEVENTEENTH_POST_NUMBER)
    assert text == DEFAULT_CHEKISTS_SEVENTEENTH_POST
    assert f"*[Точка на карте({THIRD_IDOL_URL})]*" in text
    assert "🥲" in text
