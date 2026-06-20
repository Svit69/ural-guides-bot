from src.user_panel.keyboards import UserPanelKeyboardFactory


def test_builds_user_panel_keyboard() -> None:
    keyboard = UserPanelKeyboardFactory().build_main_keyboard()

    assert keyboard.keyboard[0][0].text == "все гайды"
    assert keyboard.keyboard[1][0].text == "обратная связь"
    assert keyboard.resize_keyboard is True
