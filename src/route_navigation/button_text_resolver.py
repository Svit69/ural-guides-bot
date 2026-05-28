from src.messages.default_posts import NINTH_POST_NUMBER


class RouteButtonTextResolver:
    def resolve_button_text(self, next_post_number: int) -> str:
        button_texts = {
            NINTH_POST_NUMBER: "почему здесь стоит пяматник Куйбышеву?",
        }
        return button_texts.get(next_post_number, "идем дальше")
