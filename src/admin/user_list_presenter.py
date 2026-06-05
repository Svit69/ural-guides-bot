class UserListPresenter:
    def build_user_list_text(
        self, users: list[dict[str, str]], viz_buyer_count: int = 0
    ) -> str:
        lines = [f"Пользователей: {len(users)}", f"Купили гайд по ВИЗу: {viz_buyer_count}", ""]
        if not users:
            lines.append("В БД пока нет зарегистрированных пользователей.")
            return "\n".join(lines)
        for user in users:
            lines.append(self.__build_user_line(user))
        return "\n".join(lines)

    def build_viz_buyer_list_text(self, users: list[dict[str, str]]) -> str:
        if not users:
            return "Покупателей гайда по ВИЗу пока нет."
        lines = [f"Купили гайд по ВИЗу: {len(users)}", ""]
        for user in users:
            lines.append(self.__build_user_line(user))
        return "\n".join(lines)

    def __build_user_line(self, user: dict[str, str]) -> str:
        username = user.get("username") or "без username"
        full_name = user.get("full_name") or "без имени"
        return f"{user['telegram_id']} | @{username} | {full_name}"
