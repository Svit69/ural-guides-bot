from src.route_navigation.callbacks import RouteNavigationCallbackData
from src.route_navigation.keyboards import RouteNavigationKeyboardFactory


def test_builds_next_post_keyboard_with_readable_text() -> None:
    keyboard = RouteNavigationKeyboardFactory().build_next_post_keyboard(3)
    button = keyboard.inline_keyboard[0][0]

    assert button.text == "идем дальше"
    assert button.callback_data == "route:post:3"


def test_builds_kuibyshev_question_button() -> None:
    keyboard = RouteNavigationKeyboardFactory().build_next_post_keyboard(9)
    button = keyboard.inline_keyboard[0][0]

    assert button.text == "почему здесь стоит пяматник Куйбышеву?"
    assert button.callback_data == "route:post:9"


def test_builds_finish_walk_button() -> None:
    keyboard = RouteNavigationKeyboardFactory().build_next_post_keyboard(12)
    button = keyboard.inline_keyboard[0][0]

    assert button.text == "завершить прогулку"
    assert button.callback_data == "route:post:12"


def test_parses_route_post_callback() -> None:
    callbacks = RouteNavigationCallbackData()

    assert callbacks.parse_post_number("route:post:4") == 4
