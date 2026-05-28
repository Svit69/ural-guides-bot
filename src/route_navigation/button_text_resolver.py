from src.messages.default_posts import FINAL_POST_NUMBER, NINTH_POST_NUMBER


class RouteButtonTextResolver:
    def resolve_button_text(self, next_post_number: int) -> str:
        button_texts = {
            NINTH_POST_NUMBER: "почему здесь стоит пяматник Куйбышеву?",
            FINAL_POST_NUMBER: "завершить прогулку",
        }
        return button_texts.get(next_post_number, "идем дальше")
