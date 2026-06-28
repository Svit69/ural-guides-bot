from src.guides.chekists_library_posts import DEFAULT_CHEKISTS_THIRTY_SECOND_POST
from src.guides.chekists_posts import CHEKISTS_THIRTY_SECOND_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_thirty_second_post_is_available() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_THIRTY_SECOND_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_THIRTY_SECOND_POST
    assert "Птичка напела" in text
