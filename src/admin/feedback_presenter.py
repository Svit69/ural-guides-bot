class FeedbackPresenter:
    def build_feedback_text(self, feedback: dict[str, object]) -> str:
        text = feedback.get("text") or "Медиа без подписи"
        return (
            f"Отзыв #{feedback.get('id')}\n"
            f"От: {feedback.get('full_name')} ({feedback.get('user_id')})\n"
            f"Дата: {feedback.get('created_at')}\n\n"
            f"{text}"
        )
