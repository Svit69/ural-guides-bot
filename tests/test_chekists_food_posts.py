from src.guides.chekists_food_posts import DEFAULT_CHEKISTS_SEVENTH_POST
from src.guides.chekists_food_posts import DEFAULT_CHEKISTS_SIXTH_POST
from src.guides.chekists_food_posts import DONUT_SHOP_URL, SELF_CARE_ART_URL
from src.guides.chekists_posts import CHEKISTS_SEVENTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_SIXTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_sixth_post_is_available_from_default_catalog() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_SIXTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_SIXTH_POST
    assert "Пончиковая №1" in text
    assert DONUT_SHOP_URL in text


def test_chekists_seventh_post_is_available_from_default_catalog() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_SEVENTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_SEVENTH_POST
    assert "Берегись себя" in text
    assert SELF_CARE_ART_URL in text
