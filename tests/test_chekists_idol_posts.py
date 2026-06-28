from src.guides.chekists_idol_posts import DEFAULT_CHEKISTS_NINETEENTH_POST
from src.guides.chekists_idol_posts import FIFTH_IDOL_URL
from src.guides.chekists_posts import CHEKISTS_NINETEENTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_nineteenth_post_preserves_map_link() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_NINETEENTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_NINETEENTH_POST
    assert f"*[Задний двор Ленина, 69/13({FIFTH_IDOL_URL})]*" in text
