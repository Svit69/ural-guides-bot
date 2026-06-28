from src.guides.chekists_library_posts import DEFAULT_CHEKISTS_THIRTY_FIRST_POST
from src.guides.chekists_library_posts import LIBRARY_URL
from src.guides.chekists_posts import CHEKISTS_THIRTY_FIRST_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_thirty_first_post_preserves_library_link() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_THIRTY_FIRST_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_THIRTY_FIRST_POST
    assert f"*[Ленина, 69/9({LIBRARY_URL})]*" in text
