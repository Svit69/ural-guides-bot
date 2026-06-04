from src.payments.keyboards import VizPaymentKeyboardFactory
from src.payments.messages import build_viz_payment_error, build_viz_payment_prompt
from src.payments.yookassa_settings import YooKassaSettings


def test_rejects_unconfigured_payment_settings() -> None:
    settings = YooKassaSettings("", "", "", "")

    assert settings.is_configured() is False


def test_builds_viz_payment_keyboard() -> None:
    keyboard = VizPaymentKeyboardFactory().build_payment_keyboard("https://pay")

    assert keyboard.inline_keyboard[0][0].url == "https://pay"
    assert keyboard.inline_keyboard[1][0].callback_data == "guide:viz:payment:check"
    assert "500.00 ₽" in build_viz_payment_prompt("500.00")
    assert "Причина: invalid_credentials" in build_viz_payment_error("invalid_credentials")
