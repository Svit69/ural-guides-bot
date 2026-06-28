from src.guides.chekists_posts import CHEKISTS_FIRST_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_FIFTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_FOURTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_SECOND_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_THIRD_POST_NUMBER
from src.guides.chekists_posts import DEFAULT_CHEKISTS_FIRST_POST
from src.guides.chekists_posts import DEFAULT_CHEKISTS_SECOND_POST
from src.guides.chekists_later_posts import DEFAULT_CHEKISTS_FIFTH_POST
from src.guides.chekists_later_posts import DEFAULT_CHEKISTS_FOURTH_POST
from src.guides.chekists_later_posts import DEFAULT_CHEKISTS_THIRD_POST
from src.guides.chekists_later_posts import ISET_HOTEL_URL, RESIDENTIAL_BUILDINGS_URL
from src.guides.chekists_later_posts import WORD_OF_THE_BOY_GRAFFITI_URL
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_post_is_available_from_default_catalog() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_FIRST_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_FIRST_POST
    assert "Городок чекистов" in text


def test_chekists_second_post_is_available_from_default_catalog() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_SECOND_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_SECOND_POST
    assert "Немного вводных" in text


def test_chekists_third_post_is_available_from_default_catalog() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_THIRD_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_THIRD_POST
    assert ISET_HOTEL_URL in text


def test_chekists_fourth_post_is_available_from_default_catalog() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_FOURTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_FOURTH_POST
    assert RESIDENTIAL_BUILDINGS_URL in text


def test_chekists_fifth_post_is_available_from_default_catalog() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_FIFTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_FIFTH_POST
    assert WORD_OF_THE_BOY_GRAFFITI_URL in text
