from src.guides.chekists_art_posts import DEFAULT_CHEKISTS_TENTH_POST
from src.guides.chekists_art_posts import GRAFFITI_CLUSTER_URL
from src.guides.chekists_posts import CHEKISTS_TENTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_tenth_post_preserves_link_and_emoji() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_TENTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_TENTH_POST
    assert f"[Точку поставлю на мусорной площадке]({GRAFFITI_CLUSTER_URL})" in text
    assert "🥲" in text
    assert "▪️Граффити «Не болтай»" in text
