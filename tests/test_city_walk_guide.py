from src.guides.city_walk_post import CITY_WALK_POST_NUMBER
from src.guides.city_walk_post import DEFAULT_CITY_WALK_POST
from src.messages.default_post_catalog import DefaultPostCatalog


def test_city_walk_post_is_available_from_default_catalog() -> None:
    text = DefaultPostCatalog().get_default_text(CITY_WALK_POST_NUMBER)

    assert text == DEFAULT_CITY_WALK_POST
