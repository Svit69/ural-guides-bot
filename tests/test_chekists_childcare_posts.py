from src.guides.chekists_childcare_posts import CHILDCARE_BUILDING_URL
from src.guides.chekists_childcare_posts import DEFAULT_CHEKISTS_TWENTY_EIGHTH_POST
from src.guides.chekists_childcare_posts import DEFAULT_CHEKISTS_TWENTY_FIFTH_POST
from src.guides.chekists_childcare_posts import DEFAULT_CHEKISTS_TWENTY_FOURTH_POST
from src.guides.chekists_childcare_posts import DEFAULT_CHEKISTS_TWENTY_SEVENTH_POST
from src.guides.chekists_childcare_posts import DEFAULT_CHEKISTS_TWENTY_SIXTH_POST
from src.guides.chekists_childcare_posts import SIXTH_IDOL_URL
from src.guides.chekists_childcare_posts import SPORTS_GROUND_URL
from src.guides.chekists_posts import CHEKISTS_TWENTY_EIGHTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_TWENTY_FIFTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_TWENTY_FOURTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_TWENTY_SEVENTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_TWENTY_SIXTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_twenty_fourth_post_preserves_childcare_link() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_TWENTY_FOURTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_TWENTY_FOURTH_POST
    assert f"*[Ленина, 69/12({CHILDCARE_BUILDING_URL})]*" in text


def test_chekists_twenty_fifth_post_preserves_sports_ground_link() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_TWENTY_FIFTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_TWENTY_FIFTH_POST
    assert f"*[Точка на карте({SPORTS_GROUND_URL})]*" in text


def test_chekists_twenty_sixth_post_is_available() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_TWENTY_SIXTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_TWENTY_SIXTH_POST
    assert "офис ФСИН" in text


def test_chekists_twenty_seventh_post_preserves_sixth_idol_link() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_TWENTY_SEVENTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_TWENTY_SEVENTH_POST
    assert f"*[Точка на карте({SIXTH_IDOL_URL})]*" in text


def test_chekists_twenty_eighth_post_preserves_booth_link() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_TWENTY_EIGHTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_TWENTY_EIGHTH_POST
    assert "Большая сушка" in text
