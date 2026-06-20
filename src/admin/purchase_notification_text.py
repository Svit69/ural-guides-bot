from aiogram.types import User


class PurchaseNotificationText:
    __phrases = (
        "Отличная новость для статистики!",
        "Маршрут нашел нового путешественника.",
        "Еще одна прогулка отправилась в путь.",
        "Платный гайд приносит результат.",
        "Можно порадоваться новой покупке.",
    )

    def build_text(self, user: User, guide_name: str) -> str:
        phrase = self.__phrases[user.id % len(self.__phrases)]
        return f"{self.__build_name(user)} купил/ла {guide_name}.\n{phrase}"

    def __build_name(self, user: User) -> str:
        if user.full_name:
            return user.full_name
        return f"@{user.username}" if user.username else str(user.id)
