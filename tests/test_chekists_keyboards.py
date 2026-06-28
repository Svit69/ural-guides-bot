from src.guides.guide_ids import GUIDE_CHEKISTS
from src.guides.keyboards import GuideKeyboardFactory
from src.subscription.callbacks import SubscriptionCallbackData


def test_chekists_button_is_visible_when_guide_is_visible() -> None:
    keyboard = GuideKeyboardFactory().build_guide_selection_keyboard(
        visible_guides={GUIDE_CHEKISTS}
    )
    button = keyboard.inline_keyboard[0][0]

    assert button.text == "Городок чекистов"
    assert button.callback_data == "guide:select:chekists"


def test_builds_chekists_subscription_callback() -> None:
    callback_data = SubscriptionCallbackData.build_check_callback(GUIDE_CHEKISTS)

    assert callback_data == "subscription:check:chekists"
    assert SubscriptionCallbackData.parse_guide_id(callback_data) == GUIDE_CHEKISTS


def test_builds_chekists_next_keyboard_after_first_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard(
        "guide:chekists:next:1"
    )

    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:1"


def test_builds_chekists_next_keyboard_after_second_post() -> None:
    keyboard = GuideKeyboardFactory().build_chekists_next_keyboard(
        "guide:chekists:next:2"
    )

    assert keyboard.inline_keyboard[0][0].callback_data == "guide:chekists:next:2"
