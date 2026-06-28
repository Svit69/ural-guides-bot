class SubscriptionCallbackData:
    CHECK_PREFIX = "subscription:check:"
    CHECK_SUBSCRIPTION = "subscription:check:big_konny"

    @classmethod
    def build_check_callback(cls, guide_id: str) -> str:
        return f"{cls.CHECK_PREFIX}{guide_id}"

    @classmethod
    def parse_guide_id(cls, callback_data: str) -> str:
        return callback_data.removeprefix(cls.CHECK_PREFIX)
