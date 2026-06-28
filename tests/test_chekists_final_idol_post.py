from src.guides.chekists_childcare_posts import DEFAULT_CHEKISTS_TWENTY_NINTH_POST
from src.guides.chekists_posts import CHEKISTS_TWENTY_NINTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_twenty_ninth_post_is_available() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_TWENTY_NINTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_TWENTY_NINTH_POST
    assert "Последний идол, седьмой" in text
