from aiogram.types import User

from src.admin.purchase_notification_text import PurchaseNotificationText
from src.admin.user_list_presenter import UserListPresenter


def test_user_list_places_statistics_after_users() -> None:
    text = UserListPresenter().build_user_list_text(
        [{"telegram_id": 1, "username": "nast_bar", "full_name": "Настя"}],
        viz_buyer_count=2,
        city_buyer_count=3,
    )

    lines = text.splitlines()

    assert lines[0] == "1 | @nast_bar | Настя"
    assert lines[-3:] == [
        "Пользователей: 1",
        "Купили гайд по ВИЗу: 2",
        "Купили прогулку по Екатеринбургу: 3",
    ]


def test_purchase_notification_mentions_user_and_guide() -> None:
    user = User(id=1, is_bot=False, first_name="Настя", username="nast_bar")
    text = PurchaseNotificationText().build_text(user, "гайд по ВИЗу")

    assert "Настя купил/ла гайд по ВИЗу." in text
