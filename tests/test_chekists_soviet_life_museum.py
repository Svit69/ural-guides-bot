from src.guides.chekists_childcare_posts import DEFAULT_CHEKISTS_THIRTIETH_POST
from src.guides.chekists_childcare_posts import SOVIET_LIFE_MUSEUM_URL
from src.guides.chekists_posts import CHEKISTS_THIRTIETH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_thirtieth_post_preserves_museum_link() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_THIRTIETH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_THIRTIETH_POST
    assert f"*[Ленина, 69/6({SOVIET_LIFE_MUSEUM_URL})]*" in text
