from src.feedback.keyboards import FeedbackKeyboardFactory


def test_builds_feedback_confirmation_keyboard() -> None:
    keyboard = FeedbackKeyboardFactory().build_confirmation_keyboard()
    send_button = keyboard.inline_keyboard[0][0]
    later_button = keyboard.inline_keyboard[1][0]

    assert send_button.text == "отправить отзыв"
    assert send_button.callback_data == "feedback:send"
    assert later_button.text == "оставить отзыв позже"
    assert later_button.callback_data == "feedback:leave_later"


def test_builds_leave_later_keyboard() -> None:
    button = FeedbackKeyboardFactory().build_leave_later_keyboard().inline_keyboard[0][0]

    assert button.text == "оставить отзыв позже"
    assert button.callback_data == "feedback:leave_later"
