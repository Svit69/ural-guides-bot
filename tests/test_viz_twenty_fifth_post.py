from src.guides.viz_post_numbers import VIZ_TWENTY_FIFTH_POST_NUMBER
from src.guides.viz_twenty_fifth_post import DEFAULT_VIZ_TWENTY_FIFTH_POST
from src.guides.viz_twenty_fifth_post import OLD_LARCH_LOCATION_URL
from src.messages.default_post_catalog import DefaultPostCatalog
from src.messages.viz_late_post_catalog import VizLatePostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_viz_twenty_fifth_post_is_registered() -> None:
    late_posts = VizLatePostCatalog().get_posts()
    default_text = DefaultPostCatalog().get_default_text(VIZ_TWENTY_FIFTH_POST_NUMBER)

    assert late_posts[VIZ_TWENTY_FIFTH_POST_NUMBER] == DEFAULT_VIZ_TWENTY_FIFTH_POST
    assert default_text == DEFAULT_VIZ_TWENTY_FIFTH_POST


def test_viz_twenty_fifth_post_has_formatted_map_link() -> None:
    formatted_text = TelegramTextFormatter().format_text(DEFAULT_VIZ_TWENTY_FIFTH_POST)

    assert ">Крауля, 73</a>" in formatted_text
    assert OLD_LARCH_LOCATION_URL.replace("&", "&amp;") in formatted_text
