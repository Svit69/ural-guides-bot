from src.feedback.keyboards import FeedbackKeyboardFactory


def test_builds_feedback_confirmation_keyboard() -> None:
    keyboard = FeedbackKeyboardFactory().build_confirmation_keyboard()
    send_button = keyboard.inline_keyboard[0][0]
    edit_button = keyboard.inline_keyboard[1][0]

    assert send_button.text == "отправить отзыв"
    assert send_button.callback_data == "feedback:send"
    assert edit_button.text == "редактировать отзыв"
    assert edit_button.callback_data == "feedback:edit"
