from src.guides.chekists_posts import CHEKISTS_FIRST_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_SECOND_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_THIRD_POST_NUMBER
from src.guides.chekists_posts import DEFAULT_CHEKISTS_FIRST_POST
from src.guides.chekists_posts import DEFAULT_CHEKISTS_SECOND_POST
from src.guides.chekists_posts import DEFAULT_CHEKISTS_THIRD_POST, ISET_HOTEL_URL
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
