from src.guides.viz_post_numbers import VIZ_TWENTY_SIXTH_POST_NUMBER
from src.guides.viz_twenty_sixth_post import DEFAULT_VIZ_TWENTY_SIXTH_POST
from src.messages.default_post_catalog import DefaultPostCatalog
from src.messages.viz_late_post_catalog import VizLatePostCatalog


def test_viz_twenty_sixth_post_is_registered_as_final_text() -> None:
    late_posts = VizLatePostCatalog().get_posts()
    default_text = DefaultPostCatalog().get_default_text(VIZ_TWENTY_SIXTH_POST_NUMBER)

    assert late_posts[VIZ_TWENTY_SIXTH_POST_NUMBER] == DEFAULT_VIZ_TWENTY_SIXTH_POST
    assert default_text == "Посмотрим Гастроном 2 и завершаем маршрут"
