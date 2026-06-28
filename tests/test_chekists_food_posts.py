from src.guides.chekists_food_posts import DEFAULT_CHEKISTS_SIXTH_POST, DONUT_SHOP_URL
from src.guides.chekists_posts import CHEKISTS_SIXTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_sixth_post_is_available_from_default_catalog() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_SIXTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_SIXTH_POST
    assert "Пончиковая №1" in text
    assert DONUT_SHOP_URL in text
