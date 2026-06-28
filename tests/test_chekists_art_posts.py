from src.guides.chekists_art_posts import DEFAULT_CHEKISTS_ELEVENTH_POST
from src.guides.chekists_art_posts import DEFAULT_CHEKISTS_TENTH_POST
from src.guides.chekists_art_posts import GRAFFITI_CLUSTER_URL
from src.guides.chekists_posts import CHEKISTS_ELEVENTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_TENTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_chekists_tenth_post_preserves_link_and_emoji() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_TENTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_TENTH_POST
    assert f"[Точку поставлю на мусорной площадке]({GRAFFITI_CLUSTER_URL})" in text
    assert "🥲" in text
    assert "▪️Граффити «Не болтай»" in text


def test_chekists_eleventh_post_is_available_from_default_catalog() -> None:
    text = DefaultPostCatalog().get_default_text(CHEKISTS_ELEVENTH_POST_NUMBER)

    assert text == DEFAULT_CHEKISTS_ELEVENTH_POST
    assert "Шигирский идол" in text
    assert "Олеся Фрич" in text
