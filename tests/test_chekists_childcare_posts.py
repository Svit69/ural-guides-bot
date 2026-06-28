from src.guides.chekists_childcare_posts import CHILDCARE_BUILDING_URL
from src.guides.chekists_childcare_posts import DEFAULT_CHEKISTS_TWENTY_FOURTH_POST
from src.guides.chekists_posts import CHEKISTS_TWENTY_FOURTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_twenty_fourth_post_preserves_childcare_link() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_TWENTY_FOURTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_TWENTY_FOURTH_POST
    assert f"*[Ленина, 69/12({CHILDCARE_BUILDING_URL})]*" in text
