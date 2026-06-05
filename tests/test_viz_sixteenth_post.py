from src.guides.viz_posts import VIZ_SIXTEENTH_POST_NUMBER
from src.guides.viz_sixteenth_post import DEFAULT_VIZ_SIXTEENTH_POST
from src.messages.default_post_catalog import DefaultPostCatalog
from src.text_formatting.telegram_formatter import TelegramTextFormatter


def test_viz_sixteenth_post_is_available_and_preserves_paragraphs() -> None:
    source_text = DefaultPostCatalog().get_default_text(VIZ_SIXTEENTH_POST_NUMBER)
    formatted_text = TelegramTextFormatter().format_text(source_text)

    assert source_text == DEFAULT_VIZ_SIXTEENTH_POST
    assert "Площадь Субботников и завод\n\nИдём поесть?" in formatted_text
