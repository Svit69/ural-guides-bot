from src.guides.chekists_library_posts import DEFAULT_CHEKISTS_THIRTY_THIRD_POST
from src.guides.chekists_library_posts import LOCAL_HISTORY_MUSEUM_URL
from src.guides.chekists_posts import CHEKISTS_THIRTY_THIRD_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_thirty_third_post_preserves_museum_link() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_THIRTY_THIRD_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_THIRTY_THIRD_POST
    assert f"*[Ленина, 69/10({LOCAL_HISTORY_MUSEUM_URL})]*" in text
