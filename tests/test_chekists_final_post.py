from src.guides.chekists_final_posts import DEFAULT_CHEKISTS_THIRTY_FIFTH_POST
from src.guides.chekists_posts import CHEKISTS_THIRTY_FIFTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_final_post_is_available() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_THIRTY_FIFTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_THIRTY_FIFTH_POST
    assert "На этом всё!" in text
    assert "оставить отзыв" in text
