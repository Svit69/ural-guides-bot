class AdminCallbackData:
    USERS = "admin:users"
    VIZ_BUYERS = "admin:viz_buyers"
    CITY_BUYERS = "admin:city_buyers"
    ADD_ADMIN = "admin:add_admin"
    CANCEL = "admin:cancel"
    EDIT_CONTENT = "admin:edit_content"
    FEEDBACK = "admin:feedback"
    CLEAR_FEEDBACK = "admin:clear_feedback"
    CONFIRM_CLEAR_FEEDBACK = "admin:clear_feedback:confirm"
    KEEP_TEXT = "admin:keep_text"
    REPLACE_TEXT = "admin:replace_text"
    ADD_PHOTO = "admin:add_media"
    SKIP_PHOTO = "admin:skip_media"
    SELECT_GUIDE_PREFIX = "admin:guide:"
    SELECT_POST_PREFIX = "admin:post:"
    GUIDE_BIG_KONNY = "big_konny"
    GUIDE_VIZ = "viz"
    GUIDE_CITY_WALK = "city_walk"

    @classmethod
    def build_guide_callback(cls, guide_id: str) -> str:
        return f"{cls.SELECT_GUIDE_PREFIX}{guide_id}"

    @classmethod
    def parse_guide_id(cls, callback_data: str) -> str | None:
        if not callback_data.startswith(cls.SELECT_GUIDE_PREFIX):
            return None
        guide_id = callback_data.removeprefix(cls.SELECT_GUIDE_PREFIX)
        guide_ids = {cls.GUIDE_BIG_KONNY, cls.GUIDE_VIZ, cls.GUIDE_CITY_WALK}
        return guide_id if guide_id in guide_ids else None

    @classmethod
    def build_post_callback(cls, post_number: int) -> str:
        return f"{cls.SELECT_POST_PREFIX}{post_number}"

    @classmethod
    def parse_post_number(cls, callback_data: str) -> int | None:
        if not callback_data.startswith(cls.SELECT_POST_PREFIX):
            return None
        value = callback_data.removeprefix(cls.SELECT_POST_PREFIX)
        return int(value) if value.isdigit() else None
