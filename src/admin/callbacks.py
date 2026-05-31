class AdminCallbackData:
    USERS = "admin:users"
    ADD_ADMIN = "admin:add_admin"
    CANCEL = "admin:cancel"
    EDIT_CONTENT = "admin:edit_content"
    FEEDBACK = "admin:feedback"
    KEEP_TEXT = "admin:keep_text"
    REPLACE_TEXT = "admin:replace_text"
    ADD_PHOTO = "admin:add_media"
    SKIP_PHOTO = "admin:skip_media"
    SELECT_POST_PREFIX = "admin:post:"

    @classmethod
    def build_post_callback(cls, post_number: int) -> str:
        return f"{cls.SELECT_POST_PREFIX}{post_number}"

    @classmethod
    def parse_post_number(cls, callback_data: str) -> int | None:
        if not callback_data.startswith(cls.SELECT_POST_PREFIX):
            return None
        value = callback_data.removeprefix(cls.SELECT_POST_PREFIX)
        return int(value) if value.isdigit() else None
