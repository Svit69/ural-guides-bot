CITY_PAYMENT_NOT_CONFIGURED = "Оплата прогулки по Екатеринбургу пока не настроена. Попробуйте позже."
CITY_PAYMENT_PENDING = "Оплата пока не подтверждена. Завершите платеж и проверьте еще раз."
CITY_PAYMENT_ERROR = "Не удалось связаться с ЮKassa. Попробуйте проверить оплату позже."


def build_city_payment_prompt(price_rub: str) -> str:
    return (
        f"Гайд «Прогулка по Екатеринбургу» платный. Стоимость: {price_rub} ₽.\n\n"
        "После оплаты нажмите «Проверить оплату», и бот отправит гайд."
    )


def build_city_payment_error(reason: str) -> str:
    return f"{CITY_PAYMENT_ERROR}\n\nПричина: {reason}" if reason else CITY_PAYMENT_ERROR
