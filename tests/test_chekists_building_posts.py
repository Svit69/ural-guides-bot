from src.guides.chekists_building_posts import DEFAULT_CHEKISTS_EIGHTH_POST
from src.guides.chekists_building_posts import HOUSEHOLD_BUILDING_URL
from src.guides.chekists_posts import CHEKISTS_EIGHTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_eighth_post_is_available_from_default_catalog() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_EIGHTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_EIGHTH_POST
    assert "Хозкорпус" in text
    assert HOUSEHOLD_BUILDING_URL in text
