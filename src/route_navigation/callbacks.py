class RouteNavigationCallbackData:
    PREFIX = "route:post:"

    def build_post_callback(self, post_number: int) -> str:
        return f"{self.PREFIX}{post_number}"

    def parse_post_number(self, callback_data: str) -> int | None:
        if not callback_data.startswith(self.PREFIX):
            return None
        value = callback_data.removeprefix(self.PREFIX)
        return int(value) if value.isdigit() else None
