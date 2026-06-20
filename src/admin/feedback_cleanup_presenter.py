class FeedbackCleanupPresenter:
    def build_numbered_list(self, feedback_items: list[dict[str, object]]) -> str:
        lines = ["Отзывы для удаления:"]
        for feedback in feedback_items:
            lines.append(self.__build_feedback_line(feedback))
        lines.append("\nНапишите номера отзывов через запятую.")
        return "\n".join(lines)

    def build_confirmation_text(self, feedback_ids: list[int]) -> str:
        values = ", ".join(str(feedback_id) for feedback_id in feedback_ids)
        return f"Удалить отзывы: {values}?"

    def __build_feedback_line(self, feedback: dict[str, object]) -> str:
        text = str(feedback.get("text") or "Медиа без подписи")
        preview = text.replace("\n", " ")[:80]
        author = feedback.get("full_name") or feedback.get("user_id")
        return f"#{feedback.get('id')} | {author} | {preview}"
