class UserListPresenter:
    def build_user_list_text(self, users: list[dict[str, str]]) -> str:
        if not users:
            return "В БД пока нет зарегистрированных пользователей."
        lines = [f"Пользователей: {len(users)}", ""]
        for user in users:
            lines.append(self.__build_user_line(user))
        return "\n".join(lines)

    def __build_user_line(self, user: dict[str, str]) -> str:
        username = user.get("username") or "без username"
        full_name = user.get("full_name") or "без имени"
        return f"{user['telegram_id']} | @{username} | {full_name}"
