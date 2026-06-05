from src.guides.viz_eighteenth_post import DEFAULT_VIZ_EIGHTEENTH_POST
from src.guides.viz_post_numbers import VIZ_EIGHTEENTH_POST_NUMBER
from src.messages.default_post_catalog import DefaultPostCatalog


def test_viz_eighteenth_post_is_available() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_EIGHTEENTH_POST_NUMBER)

    assert source_text == DEFAULT_VIZ_EIGHTEENTH_POST
